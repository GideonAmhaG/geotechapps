"""
Module for storing all functions used to calculate values
"""
import math


pi = math.pi

def valid_inputs(DL, LL, mxp, mxv, myp, myv, colx, coly, fck, fyk, bar, soil_type,
    phi_f=None, cu=None, Df=None, gamma=None, bc=None):
    """
    Checks if the provided input values are within acceptable ranges.
    """
    valid_range = lambda val, min_val, max_val: min_val <= val <= max_val
    base_checks = (valid_range(DL, 200, 4100) and
            valid_range(LL, 130, 2100) and
            valid_range(colx, 0.1, 1.5) and
            valid_range(mxp, -2000, 2000) and
            valid_range(mxv, -2000, 2000) and
            valid_range(myp, -2000, 2000) and
            valid_range(myv, -2000, 2000) and
            valid_range(fck, 25, 100) and
            valid_range(fyk, 100, 1000) and
            valid_range(bar, 12, 32) and
            valid_range(coly, 0.1, 1.5))
    if soil_type == "clay":
        clay_checks = (valid_range(cu, 1, 1000) and
            valid_range(Df, 0, 10) and
            valid_range(gamma, 1, 30))  
        return base_checks and clay_checks
    elif soil_type == "sand":
        sand_checks = (valid_range(phi_f, 1, 70) and
            valid_range(Df, 0, 10) and
            valid_range(gamma, 1, 30))  
        return base_checks and sand_checks
    elif soil_type == "bearing_c":
        bc_checks = valid_range(bc, 50, 1000)  
        return base_checks and bc_checks
    return False

def d_avg(D, phi, cov):
    d = ((D - cov - phi - (phi / 2)) + (D - cov - phi)) / 2
    return d

def kay(D, phi, cover):
    d = d_avg(D, phi, cover)
    k = 1 + ((200 / (d * 1000)) ** 0.5)
    # print(k)
    if k <= 2:
        return k
    else:
        return 2

def area_part2_punch(D, phi, B, colx, coly, cover):
    d = d_avg(D, phi, cover)
    Ap2 = (B * B) - ((((4 * d) + coly) * colx) + (4 * d * coly) + (pi * d * d * 4))
    if Ap2 > 0:
        return Ap2
    else:
        return 0

def area_part2_wide(D, phi, B, col, cover):
    d = d_avg(D, phi, cover)
    Ap2 = ((B / 2) - (col / 2) - d) * B
    if Ap2 > 0:
        return Ap2
    else:
        return 0

def ved_vrd_wide(D, phi, fck, B, col, sig_s, rho, cover):
    d = d_avg(D, phi, cover)
    k = kay(D, phi, cover)
    vrd_a = (0.12 * k * ((100 * rho * fck) ** (1 / 3))) * 1000
    vrd_min = (0.035 * (k ** 1.5) * (fck ** 0.5)) * 1000
    vrd = max(vrd_a, vrd_min)
    Ap2_wide = area_part2_wide(D, phi, B, col, cover)
    As_wide = B * d
    ved_wide = (sig_s * Ap2_wide) / As_wide
    return ved_wide, vrd, k, vrd_min, Ap2_wide, As_wide

def ved_vrd_punch(D, phi, fck, B, colx, coly, sig_s, rho, cover):
    d = d_avg(D, phi, cover)
    k = kay(D, phi, cover)
    vrd_a = (0.12 * k * ((100 * rho * fck) ** (1 / 3))) * 1000
    vrd_min = (0.035 * (k ** 1.5) * (fck ** 0.5)) * 1000
    vrd = max(vrd_a, vrd_min)
    Ap2_punch = area_part2_punch(D, phi, B, colx, coly, cover)
    As_punch = ((2 * colx) + (2 * coly) + (4 * pi * d)) * d
    ved_punch = (sig_s * Ap2_punch) / As_punch
    return ved_punch, vrd, k, vrd_min, Ap2_punch, As_punch

def terzaghi(phi):
    phi_r = math.radians(phi)
    Nq = math.exp(((270-phi)/180)*math.pi*math.tan(phi_r))/(2*(math.cos(math.radians(45+(phi/2))))**2)
    Nc = (Nq-1)/(math.tan(phi_r))
    Ngamma = (2*(Nq+1)*math.tan(phi_r))/(1+(0.4*math.sin(math.radians(4*phi))))
    return Nc, Nq, Ngamma

def sig_prop(B, D, col, DL, LL, mxp, mxv, myp, myv, soil_type, Df=None, phi_f=None, cu=None,
        gamma=None, bc=None):
    if soil_type == 'bearing_c':
        Df = 3
    SW_conc = 24 * B * B * D
    SW_fill = (((B * B) - (col * col))) * Df * 0
    SW = SW_conc + SW_fill
    p_p = DL + SW + LL
    ex = abs((myp + myv) / p_p)
    ey = abs((mxp + mxv) / p_p)
    sig_p = (p_p / (B * B)) * (1 + ((6 * ex) / B) + ((6 * ey) / B))
    FS = 3
    if soil_type == "clay":
        qu = (1.3 * cu * 5.7) + (gamma * Df)
        qa = qu / FS
        return sig_p, qa, ex, ey, SW_conc, SW_fill
    elif soil_type == "sand":
        Nc, Nq, Ngamma = terzaghi(phi_f)
        qu = (gamma * Df * Nq) + (0.4 * B * gamma * Ngamma)
        qa = qu / FS
        return sig_p, qa, ex, ey, SW_conc, SW_fill, Nc, Nq, Ngamma
    elif soil_type == "bearing_c":
        qa = bc
        return sig_p, qa, ex, ey, SW_conc, SW_fill
    return None

def zed(D, phi, m, B, fck, cover):
    d = d_avg(D, phi, cover)
    z = d * (0.5 + (0.25 - (m / (B * (d ** 2) * (fck * 1000) * 1.134))) ** 0.5)
    return z

def med_mrd(sig_s, B, col, D, phi, fck, rho, rho_min, fyk, cover):
    med = sig_s * (B / 2) * ((B / 2 - col / 2) ** 2)
    z = zed(D, phi, med, B, fck, cover)
    d = d_avg(D, phi, cover)
    rho = max(rho, rho_min)
    mrd = 0.87 * (fyk * 1000) * z * rho * B * d
    return med, mrd, z

def iter_b(B, D, col, DL, LL, mxp, mxv, myp, myv, soil_type, Df,
        cu=None, phi_f=None, bc=None, gamma=None):
    if soil_type == 'bearing_c':
        Df = 3
    tolerance = 0.00005
    diff = 0.01
    if soil_type == "sand":
        sig_p, qa, ex, ey, SW_conc, SW_fill, Nc, Nq, Ngamma = sig_prop(B, D, col, DL,
            LL, mxp, mxv, myp, myv, soil_type, Df=Df, phi_f=phi_f, gamma=gamma)
        while abs(sig_p - qa) > diff:
            if sig_p > qa:
                B += tolerance
            else:
                B -= tolerance
            sig_p, qa, ex, ey, SW_conc, SW_fill, Nc, Nq, Ngamma = sig_prop(B, D, col, DL,
                LL, mxp, mxv, myp, myv, soil_type, Df=Df, phi_f=phi_f, gamma=gamma)
        return sig_p, qa, ex, ey, SW_conc, SW_fill, Nc, Nq, Ngamma, B
    else:
        sig_p, qa, ex, ey, SW_conc, SW_fill = sig_prop(B, D, col, DL, LL, mxp, mxv,
            myp, myv, soil_type, Df=Df, cu=cu if soil_type == "clay" else None,
            gamma=gamma if soil_type == "clay" else None, bc=bc if soil_type != "clay" else None)
        while abs(sig_p - qa) > diff:
            if sig_p > qa:
                B += tolerance
            else:
                B -= tolerance
            sig_p, qa, ex, ey, SW_conc, SW_fill = sig_prop(B, D, col, DL, LL, mxp, mxv,
                myp, myv, soil_type, Df, cu=cu if soil_type == "clay" else None,
                gamma=gamma if soil_type == "clay" else None, bc=bc if soil_type != "clay" else None)
        return sig_p, qa, ex, ey, SW_conc, SW_fill, B
