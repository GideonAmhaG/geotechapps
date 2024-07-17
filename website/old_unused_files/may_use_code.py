            # if iter_b doesn't work
            # if soil_type == "clay":
            #     sig_p, qa, ex, ey, SW_conc, SW_fill = sig_prop(B, D, col,
            #         Df, DL, LL, mxp, mxv, myp, myv, cu, gamma)
            #     if sig_p > qa:
            #         while sig_p > qa:
            #             sig_p, qa, ex, ey, SW_conc, SW_fill = sig_prop(B, D, col, Df,
            #                 DL, LL, mxp, mxv, myp, myv, cu, gamma)
            #             B += 0.000005
            #     else:
            #         while sig_p <= qa:
            #             sig_p, qa, ex, ey, SW_conc, SW_fill = sig_prop(B, D, col, Df, 
            #                 DL, LL, mxp, mxv, myp, myv, cu, gamma)
            #             B -= 0.000005
            # if soil_type == "sand":
            #     sig_p, qa, ex, ey, SW_conc, SW_fill, Nc, Nq, Ngamma = sig_prop(B,
            #         D, col, Df, DL, LL, mxp, mxv, myp, myv, phi_f, gamma)
            #     if sig_p > qa:
            #         while sig_p > qa:
            #             sig_p, qa, ex, ey, SW_conc, SW_fill, Nc, Nq, Ngamma = sig_prop(B,
            #                 D, col, Df, DL, LL, mxp, mxv, myp, myv, phi_f, gamma)
            #             B += 0.000005
            #     else:
            #         while sig_p <= qa:
            #             sig_p, qa, ex, ey, SW_conc, SW_fill, Nc, Nq, Ngamma = sig_prop(B,
            #                 D, col, Df, DL, LL, mxp, mxv, myp, myv, phi_f, gamma)
            #             B -= 0.000005
            # if soil_type == "bearing_c":
            #     sig_p, qa, ex, ey, SW_conc, SW_fill = sig_prop(B, D, col, Df, DL, LL, mxp,
            #         mxv, myp, myv, bc)
            #     if sig_p > qa:
            #         while sig_p > qa:
            #             sig_p, qa, ex, ey, SW_conc, SW_fill = sig_prop(B, D, col, Df, DL,
            #                 LL, mxp, mxv, myp, myv, bc)
            #             B += 0.000005
            #     else:
            #         while sig_p <= qa:
            #             sig_p, qa, ex, ey, SW_conc, SW_fill = sig_prop(B, D, col, Df, DL,
            #                 LL, mxp, mxv, myp, myv, bc)
            #             B -= 0.000005
            # com_vars = [D, B, rho, p_s, ex, ey, sig_p, D_wide, D_punch, ved_wide,
            #     ved_punch, vrd, med, mrd, SW_conc, SW_fill, sig_s, d_wide, d_punch,
            #     vrd_wide, vrd_punch, k_wide, vrd_min_wide, Ap2_wide, As_wide, k_punch,
            #     vrd_min_punch, Ap2_punch, As_punch, z]
            # if soil_type == "clay":
            #     clay_vars = [q_all, FOS]
            #     return com_vars + clay_vars
            # elif soil_type == "sand":
            #     sand_vars = [q_all, FOS, Nc, Nq, Ngamma]
            #     return com_vars + sand_vars
            # else: 
            #     return com_vars