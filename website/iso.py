""" for sand soil """
import math
from .calc_funcs import *


def iso(DL, LL, mxp, mxv, myp, myv, colx, coly, fck, fyk, bar, covr, soil_type,
        cu=None, phi_f=None, Df=None, gamma=None, bc=None):
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

    valid = False
    if soil_type == "clay":
        r_bool = valid_inputs(DL, LL, mxp, mxv, myp, myv, colx, coly, fck, fyk, bar, soil_type,
            cu=cu, Df=Df, gamma=gamma)
        valid = valid or r_bool
    elif soil_type == "sand":
        r_bool = valid_inputs(DL, LL, mxp, mxv, myp, myv, colx, coly, fck, fyk, bar, soil_type,
            phi_f=phi_f, Df=Df, gamma=gamma)
        valid = valid or r_bool
    elif soil_type == "bearing_c":
        r_bool = valid_inputs(DL, LL, mxp, mxv, myp, myv, colx, coly, fck, fyk, bar, soil_type, bc=bc)
        valid = valid or r_bool
    if valid:
        #main function
        def B_D_rho(D, D_tmp, DL, LL, mxp, mxv, myp, myv, B, fyk, rho, rho_min):
            if soil_type == "sand":
                sig_p, qa, ex, ey, SW_conc, SW_fill, Nc, Nq, Ngamma, B = iter_b(B, D, col,
                    DL, LL, mxp, mxv, myp, myv, soil_type, Df=Df, phi_f=phi_f, gamma=gamma)
            else:
                sig_p, qa, ex, ey, SW_conc, SW_fill, B = iter_b(B, D, col, DL, LL, mxp, mxv,
                    myp, myv, soil_type, Df=Df, cu=cu if soil_type == "clay" else None,
                    gamma=gamma if soil_type == "clay" else None, bc=bc if soil_type != "clay" else None)
            q_all = math.ceil(qa * 10) / 10
            FOS = 3
            qultm = q_all * FOS 
            q_ult = math.ceil(qultm * 10) / 10
            p_s = (1.35 * DL) + (1.5 * LL)
            sig_s = p_s / (B * B)
            ved_wide, vrd, k_wide, vrd_min_wide, Ap2_wide, As_wide = ved_vrd_wide(D, phi, fck,
                B, col, sig_s, rho, cover)
            ved_punch, vrd, k_punch, vrd_min_punch, Ap2_punch, As_punch = ved_vrd_punch(D, phi,
                fck, B, colx, coly, sig_s, rho, cover)
            vrd_start = vrd
            if ved_wide <= vrd:
                while ved_wide <= vrd:
                    ved_wide, vrd, k_wide, vrd_min_wide, Ap2_wide, As_wide = ved_vrd_wide(D, phi,
                        fck, B, col, sig_s, rho, cover)
                    D -= 0.000005
            else:
                while ved_wide >= vrd:
                    ved_wide, vrd, k_wide, vrd_min_wide, Ap2_wide, As_wide= ved_vrd_wide(D, phi,
                        fck, B, col, sig_s, rho, cover)
                    D += 0.000005
            D_wide = D
            d_wide = d_avg(D_wide, phi, cover)
            D = D_tmp
            vrd_wide = vrd
            vrd = vrd_start
            if ved_punch <= vrd:
                while ved_punch <= vrd:
                    ved_punch, vrd, k_punch, vrd_min_punch, Ap2_punch, As_punch = ved_vrd_punch(D,
                        phi, fck, B, colx, coly, sig_s, rho, cover)
                    D -= 0.0005
            else:
                while ved_punch >= vrd:
                    ved_punch, vrd, k_punch, vrd_min_punch, Ap2_punch, As_punch = ved_vrd_punch(D,
                        phi, fck, B, colx, coly, sig_s, rho, cover)
                    D += 0.0005
            D_punch = D
            d_punch = d_avg(D_punch, phi, cover)
            vrd_punch = vrd
            D = max(max(D_wide, D_punch), 0.3)
            med, mrd, z = med_mrd(sig_s, B, col, D, phi, fck, rho, rho_min, fyk, cover)
            if med < mrd:
                while med <= mrd:
                    med, mrd, z = med_mrd(sig_s, B, col, D, phi, fck, rho, rho_min, fyk, cover)
                    rho -= 0.0000005
            else:
                while med >= mrd:
                    med, mrd, z = med_mrd(sig_s, B, col, D, phi, fck, rho, rho_min, fyk, cover)
                    rho += 0.0000005
            com_vars = [D, B, rho, p_s, ex, ey, sig_p, D_wide, D_punch, ved_wide, ved_punch,\
                vrd, med, mrd, SW_conc, SW_fill, sig_s, d_wide, d_punch, vrd_wide, vrd_punch, k_wide,\
                vrd_min_wide, Ap2_wide, As_wide, k_punch, vrd_min_punch, Ap2_punch, As_punch, z]
            if soil_type == "clay":
                clay_vars = [q_all, q_ult, FOS]
                return com_vars + clay_vars
            elif soil_type == 'sand':
                sand_vars = [q_all, q_ult, FOS, Nc, Nq, Ngamma]
                return com_vars + sand_vars
            else:
                return com_vars
            
        res = B_D_rho(D_initial, D_initial, DL, LL, mxp, mxv, myp, myv, B_initial,
            fyk, rho_initial, rho_min)
        print(res)
        for _ in range(5):
            res = B_D_rho(res[0], res[0], DL, LL, mxp, mxv, myp, myv, res[1], fyk, res[2], rho_min)
        D_final, B_final, rho_final, p_s, ex, ey, sig_p, D_wide, D_punch, ved_wide, ved_punch,\
            vrd, med, mrd, SW_conc, SW_fill, sig_s, d_wide, d_punch, vrd_wide, vrd_punch, k_wide,\
            vrd_min_wide, Ap2_wide, As_wide, k_punch, vrd_min_punch, Ap2_punch, As_punch, z = res[:30]
        if soil_type == "clay":
            q_all, q_ult, FOS = res[30:]  
        elif soil_type == "sand":  
            q_all, q_ult, FOS, Nc, Nq, Ngamma = res[30:]  
        d_final = d_avg(D_final, phi, cover)
        As = rho_final * B_final * d_final * 1000000
        Asmin = rho_min * B_final * d_final * 1000000
        N = math.ceil(As / (math.pi * (((phi / 2) * 1000) ** 2)))
        As_f = round((N * (math.pi * (((phi / 2) * 1000) ** 2))), 1)
        B_f = math.ceil(B_final * 10) / 10
        s_a = ((B_f / (N - 1)) - phi - (cover_side * 2)) * 1000
        s_ini = math.floor(s_a / 10) * 10
        D_f = max((round((math.ceil(D_final / 0.05) * 0.05), 2)), 0.3)
        s = min(s_ini, 400, (3 * D_f * 1000))
        s_f = max(s, 20, phi)
        com_vals = {'b': B_f, 'd': D_f, 'As': As_f, 'N': N, 's': s_f, 'p_s': p_s, 'ex': ex, 'ey': ey,
            'sig_p': sig_p, 'D_wide': D_wide, 'D_punch': D_punch, 'ved_wide': ved_wide, 'ved_punch': ved_punch,
            'vrd': vrd, 'med': med, 'mrd': mrd, 'rho_min': rho_min, 'SW_conc': SW_conc, 'SW_fill': SW_fill,
            'B_final': B_final, 'D_final': D_final, 'd_final': d_final, 'sig_s': sig_s, 'd_wide': d_wide,
            'd_punch': d_punch, 'vrd_wide': vrd_wide, 'vrd_punch': vrd_punch, 'k_wide': k_wide,
            'vrd_min_wide': vrd_min_wide, 'Ap2_wide': Ap2_wide, 'As_wide': As_wide, 'k_punch': k_punch,
            'vrd_min_punch': vrd_min_punch, 'Ap2_punch': Ap2_punch, 'As_punch': As_punch, 'rho_final': rho_final,
            'z': z, 'As_old': As, 'Asmin': Asmin}
        if soil_type == "clay":
            clay_vals = {'qa': q_all, 'qu': q_ult, 'fs': FOS }
            return {**com_vals, **clay_vals}
        elif soil_type == "sand":
            sand_vals = {'qa': q_all, 'qu': q_ult, 'fs': FOS, 'Nc': Nc, 'Nq': Nq, 'Ngamma': Ngamma}
            return {**com_vals, **sand_vals}
        else:
            return com_vals
    else:
        return {}
