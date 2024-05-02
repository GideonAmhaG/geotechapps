""" for sand soil """
import math

def sand_iso(DL, LL, mxp, mxv, myp, myv, colx, coly, phi_f, Df, gamma, fck, fyk, bar, covr):
    #variables
    pi = math.pi
    col = min(colx, coly)
    B_initial = col
    D_initial = 0.7
    phi = bar / 1000
    rho_initial = 0.0025
    rho_min = max((0.26 * (1.43 / fyk) * 0.21 * (fck ** (2 / 3))) , 0.0013)
    cover = covr / 1000
    cover_side = 0.075

    if DL >= 200 and DL <= 4100 and LL >= 130 and LL <= 2100 and colx >= 0.1\
            and mxp >= -2000 and mxp <= 2000 and mxv >= -2000 and mxv <= 2000\
            and myp >= -2000 and myp <= 2000 and myv >= -2000 and myv <= 2000\
            and colx <= 1.5 and phi_f >= 1 and phi_f <= 70 and fck >= 25\
            and fck <= 100 and fyk >= 100 and fyk <= 1000 and bar >= 12\
            and bar <= 32 and Df > 0 and Df <= 10 and gamma > 1\
            and gamma <= 30 and coly >= 0.1 and coly <= 1.5:
        #functions
        def d_avg(D, phi, cov):
            d = ((D - cov - phi - (phi / 2)) + (D - cov - phi)) / 2
            return d
        def kay(D, phi):
            d = d_avg(D, phi, cover)
            k = 1 + ((200 / (d * 1000)) ** 0.5)
            if k <= 2:
                return k
            else:
                return 2
        def area_part2_punch(D, phi, B, colx, coly):
            d = d_avg(D, phi, cover)
            Ap2 = (B * B) - ((((4 * d) + coly) * colx) + (4 * d * coly) + (pi * d * d * 4))
            if Ap2 > 0:
                return Ap2
            else:
                return 0
        def area_part2_wide(D, phi, B, col):
            d = d_avg(D, phi, cover)
            Ap2 = ((B / 2) - (col / 2) - d) * B
            if Ap2 > 0:
                return Ap2
            else:
                return 0
        def ved_vrd_wide(D, phi, fck, B, col, sig_s, rho):
            d = d_avg(D, phi, cover)
            k = kay(D, phi)
            vrd_a = (0.12 * k * ((100 * rho * fck) ** (1 / 3))) * 1000
            vrd_min = (0.035 * (k ** 1.5) * (fck ** 0.5)) * 1000
            vrd = max(vrd_a, vrd_min)
            Ap2_wide = area_part2_wide(D, phi, B, col)
            As_wide = B * d
            ved_wide = (sig_s * Ap2_wide) / As_wide
            return ved_wide, vrd, k, vrd_min, Ap2_wide, As_wide
        def ved_vrd_punch(D, phi, fck, B, colx, coly, sig_s, rho):
            d = d_avg(D, phi, cover)
            k = kay(D, phi)
            vrd_a = (0.12 * k * ((100 * rho * fck) ** (1 / 3))) * 1000
            vrd_min = (0.035 * (k ** 1.5) * (fck ** 0.5)) * 1000
            vrd = max(vrd_a, vrd_min)
            Ap2_punch = area_part2_punch(D, phi, B, colx, coly)
            As_punch = ((2 * colx) + (2 * coly) + (4 * pi * d)) * d
            ved_punch = (sig_s * Ap2_punch) / As_punch
            return ved_punch, vrd, k, vrd_min, Ap2_punch, As_punch
        def terzaghi(phi):
            phi_r = math.radians(phi)
            Nq = math.exp(((270-phi)/180)*math.pi*math.tan(phi_r))/(2*(math.cos(math.radians(45+(phi/2))))**2)
            Nc = (Nq-1)/(math.tan(phi_r))
            Ngamma = (2*(Nq+1)*math.tan(phi_r))/(1+(0.4*math.sin(math.radians(4*phi))))
            return Nc, Nq, Ngamma
        def sig_prop(B, D, col, Df, DL, LL, mxp, mxv, myp, myv, phi, gamma):
            SW_conc = 24 * B * B * D
            SW_fill = (((B * B) - (col * col))) * Df * 0
            SW = SW_conc + SW_fill
            p_p = DL + SW + LL
            ex = abs((myp + myv) / p_p)
            ey = abs((mxp + mxv) / p_p)
            sig_p = (p_p / (B * B)) * (1 + ((6 * ex) / B) + ((6 * ey) / B))
            Nc, Nq, Ngamma = terzaghi(phi)
            qu = (gamma * Df * Nq) + (0.4 * B * gamma * Ngamma)
            FS = 3
            qa = qu / FS
            return sig_p, qa, ex, ey, SW_conc, SW_fill, Nc, Nq, Ngamma
        def zed(D, phi, m, B, fck):
            d = d_avg(D, phi, cover)
            z = d * (0.5 + (0.25 - (m / (B * (d ** 2) * (fck * 1000) * 1.134))) ** 0.5)
            return z
        def med_mrd(sig_s, B, col, D, phi, fck, rho, rho_min, fyk):
            med = sig_s * (B / 2) * ((B / 2 - col / 2) ** 2)
            z = zed(D, phi, med, B, fck)
            d = d_avg(D, phi, cover)
            rho = max(rho, rho_min)
            mrd = 0.87 * (fyk * 1000) * z * rho * B * d
            return med, mrd, z

        #main function
        def B_D_rho(D, D_tmp, DL, LL, mxp, mxv, myp, myv, B, fyk, rho, rho_min):
            sig_p, qa, ex, ey, SW_conc, SW_fill, Nc, Nq, Ngamma = sig_prop(B, D, col, Df, DL, LL, mxp, mxv, myp, myv, phi_f, gamma)
            q_all = math.ceil(qa * 10) / 10
            FOS = 3
            qultm = q_all * FOS 
            q_ult = math.ceil(qultm * 10) / 10
            if sig_p > qa:
                while sig_p > qa:
                    sig_p, qa, ex, ey, SW_conc, SW_fill, Nc, Nq, Ngamma = sig_prop(B, D, col, Df, DL, LL, mxp, mxv, myp, myv, phi_f, gamma)
                    B += 0.000005
            else:
                while sig_p <= qa:
                    sig_p, qa, ex, ey, SW_conc, SW_fill, Nc, Nq, Ngamma = sig_prop(B, D, col, Df, DL, LL, mxp, mxv, myp, myv, phi_f, gamma)
                    B -= 0.000005
            p_s = (1.35 * DL) + (1.5 * LL)
            sig_s = p_s / (B * B)
            ved_wide, vrd, k_wide, vrd_min_wide, Ap2_wide, As_wide = ved_vrd_wide(D, phi, fck, B, col, sig_s, rho)
            ved_punch, vrd, k_punch, vrd_min_punch, Ap2_punch, As_punch = ved_vrd_punch(D, phi, fck, B, colx, coly, sig_s, rho)
            vrd_start = vrd
            if ved_wide <= vrd:
                while ved_wide <= vrd:
                    ved_wide, vrd, k_wide, vrd_min_wide, Ap2_wide, As_wide = ved_vrd_wide(D, phi, fck, B, col, sig_s, rho)
                    D -= 0.000005
            else:
                while ved_wide >= vrd:
                    ved_wide, vrd, k_wide, vrd_min_wide, Ap2_wide, As_wide= ved_vrd_wide(D, phi, fck, B, col, sig_s, rho)
                    D += 0.000005
            D_wide = D
            d_wide = d_avg(D_wide, phi, cover)
            D = D_tmp
            vrd_wide = vrd
            vrd = vrd_start
            if ved_punch <= vrd:
                while ved_punch <= vrd:
                    ved_punch, vrd, k_punch, vrd_min_punch, Ap2_punch, As_punch = ved_vrd_punch(D, phi, fck, B, colx, coly, sig_s, rho)
                    D -= 0.0005
            else:
                while ved_punch >= vrd:
                    ved_punch, vrd, k_punch, vrd_min_punch, Ap2_punch, As_punch = ved_vrd_punch(D, phi, fck, B, colx, coly, sig_s, rho)
                    D += 0.0005
            D_punch = D
            d_punch = d_avg(D_punch, phi, cover)
            vrd_punch = vrd
            med, mrd, z = med_mrd(sig_s, B, col, D, phi, fck, rho, rho_min, fyk)
            if med < mrd:
                while med <= mrd:
                    med, mrd, z = med_mrd(sig_s, B, col, D, phi, fck, rho, rho_min, fyk)
                    rho -= 0.0000005
            else:
                while med >= mrd:
                    med, mrd, z = med_mrd(sig_s, B, col, D, phi, fck, rho, rho_min, fyk)
                    rho += 0.0000005
            return D, B, rho, q_all, FOS, q_ult, p_s, ex, ey, sig_p, D_wide, D_punch, ved_wide,\
                    ved_punch, vrd, med, mrd, SW_conc, SW_fill, sig_s, d_wide, d_punch,\
                    vrd_wide, vrd_punch, k_wide, vrd_min_wide, Ap2_wide, As_wide,\
                    k_punch, vrd_min_punch, Ap2_punch, As_punch, z, Nc, Nq, Ngamma

        D_final, B_final, rho_final, q_all, FOS, q_ult, p_s, ex, ey, sig_p, D_wide, D_punch, ved_wide,\
                    ved_punch, vrd, med, mrd, SW_conc, SW_fill, sig_s, d_wide, d_punch,\
                    vrd_wide, vrd_punch, k_wide, vrd_min_wide, Ap2_wide, As_wide,\
                    k_punch, vrd_min_punch, Ap2_punch, As_punch, z, Nc, Nq, Ngamma\
                        = B_D_rho(D_initial, D_initial, DL, LL, mxp, mxv,\
                            myp, myv, B_initial, fyk, rho_initial, rho_min)
        if D_final != D_initial or B_final != B_initial or rho_final != rho_initial:
            D_final, B_final, rho_final, q_all, FOS, q_ult, p_s, ex, ey, sig_p, D_wide, D_punch, ved_wide,\
                    ved_punch, vrd, med, mrd, SW_conc, SW_fill, sig_s, d_wide, d_punch,\
                    vrd_wide, vrd_punch, k_wide, vrd_min_wide, Ap2_wide, As_wide,\
                    k_punch, vrd_min_punch, Ap2_punch, As_punch, z, Nc, Nq, Ngamma\
                        = B_D_rho(D_final, D_final, DL, LL, mxp, mxv, myp,\
                            myv, B_final, fyk, rho_final, rho_min)
            d_final = d_avg(D_final, phi, cover)
            As = rho_final * B_final * d_final * 1000000
            Asmin = rho_min * B_final * d_final * 1000000
            N = math.ceil(As / (math.pi * (((phi / 2) * 1000) ** 2)))
            As_f = round((N * (math.pi * (((phi / 2) * 1000) ** 2))), 1)
            # B_f = round((math.ceil(B_final / 0.05) * 0.05), 2)
            B_f = math.ceil(B_final * 10) / 10
            s_a = ((B_f / (N - 1)) - phi - (cover_side * 2)) * 1000
            s_ini = math.floor(s_a / 10) * 10
            D_f = round((math.ceil(D_final / 0.05) * 0.05), 2)
            s = min(s_ini, 400, (3 * D_f * 1000))
            s_f = max(s, 20, phi)
        return [B_f, D_f, As_f, N, s_f, q_all, FOS, q_ult, p_s, ex, ey, sig_p, D_wide, D_punch, ved_wide,\
                ved_punch, vrd, med, mrd, rho_min, SW_conc, SW_fill, B_final, D_final,\
                d_final, sig_s, d_wide, d_punch, vrd_wide, vrd_punch, k_wide, vrd_min_wide,\
                Ap2_wide, As_wide, k_punch, vrd_min_punch, Ap2_punch, As_punch, rho_final, z, As, Asmin, Nc, Nq, Ngamma]
    else:
        return [0] * 45
