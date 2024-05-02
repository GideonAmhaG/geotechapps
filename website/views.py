""" main views module """


from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Note
from . import db
import json
from .bearing_c import bearing_c_iso
from .clay import clay_iso
from .sand import sand_iso

views = Blueprint('views', __name__)


@views.route('/')
def home():
    """ for home page """
    return render_template('home.html', user=current_user)


@views.route('/about')
def about():
    """ for abouts page """
    return render_template('about.html', user=current_user)


@views.route('/faq')
def faq():
    """ for FAQ page """
    return render_template('faq.html', user=current_user)


@views.route('/found_type', methods=['GET', 'POST'])
def found_type():
    """ allows selection of foundation type """
    if request.method == 'POST': 
        option = request.form['option']
        if option == 'iso_square':
            return redirect(url_for('views.soil_type'))
    return render_template('found_type.html', user=current_user)


@views.route('/soil_type', methods=['GET', 'POST'])
def soil_type():
    """ allows selection of soil type """
    if request.method == 'POST': 
        option = request.form['option']
        if option == 'clay':
            return render_template('clay.html', user=current_user)
        elif option == 'sand':
            return render_template('sand.html', user=current_user)
        elif option == 'bearing_c':
            return render_template('bearing_c.html', user=current_user)
    return render_template('soil_type.html', user=current_user)


@views.route('/clay_soil_results', methods=['POST'])
def clay_soil_results():
    """ takes inputs and displays results for clay soil """
    dl = request.form['DL']
    ll = request.form['LL']
    mxp = request.form['mxp']
    mxv = request.form['mxv']
    myp = request.form['myp']
    myv = request.form['myv']
    col = request.form['COL']
    coly = request.form['COLY']
    cu = request.form['CU']
    df = request.form['DF']
    gam = request.form['GAM']
    fck = request.form['FCK']
    fyk = request.form['FYK']
    bar = request.form['BAR']
    cov = request.form['COV']
    var_list = [dl, ll, mxp, mxv, myp, myv, col, coly, cu, df, gam, fck, fyk, bar, cov]
	
    def is_float(value):
        try:
            float(value)
            return True
        except ValueError:
            return False
	
    if any(not var for var in var_list):
        flash('An input field is blank.', category='error')
    elif any(not is_float(var) for var in var_list):    
        flash('An input field is not a number.', category='error')
    else:
        dl = float(request.form['DL'])
        ll = float(request.form['LL'])
        mxp = float(request.form['mxp'])
        mxv = float(request.form['mxv'])
        myp = float(request.form['myp'])
        myv = float(request.form['myv'])
        col = float(request.form['COL'])
        coly = float(request.form['COLY'])
        cu = float(request.form['CU'])
        df = float(request.form['DF'])
        gam = float(request.form['GAM'])
        fck = float(request.form['FCK'])
        fyk = float(request.form['FYK'])
        bar = float(request.form['BAR'])
        cov = float(request.form['COV'])
        submit_type = request.form['submit_type']
        user = current_user
        b, d, As, N, s, qa, fs, qu, p_s, ex, ey, sig_p, D_wide, D_punch, ved_wide,\
            ved_punch, vrd, med, mrd, rho_min, SW_conc, SW_fill, B_final,\
            D_final, d_final, sig_s, d_wide, d_punch, vrd_wide, vrd_punch,\
            k_wide, vrd_min_wide, Ap2_wide, As_wide, k_punch, vrd_min_punch,\
            Ap2_punch, As_punch, rho_final, z, As_old, Asmin\
                = clay_iso(dl, ll, mxp, mxv, myp, myv, col, coly, cu, df, gam, fck, fyk, bar, cov)
        if submit_type == 'regular':
            if b == 0:
                return render_template('result.html', text="You", user=current_user)
            else:
                return render_template('result.html', b=b, d=d, As=As, N=N, s=s,\
                            qa=qa, fs=fs, qu=qu, dl=dl, ll=ll, mxp=mxp, mxv=mxv, myp=myp, myv=myv,\
                            col=col, coly=coly, cu=cu, df=df, gam=gam, fck=fck,\
                            fyk=fyk, bar=bar, cov=cov, p_s=p_s, ex=ex, ey=ey, sig_p=sig_p, D_wide=D_wide,\
                            D_punch=D_punch, ved_wide=ved_wide, ved_punch=ved_punch, vrd=vrd, med=med,\
                            mrd=mrd, rho_min=rho_min, SW_conc=SW_conc, SW_fill=SW_fill, B_final=B_final,\
                            D_final=D_final, d_final=d_final, sig_s=sig_s, d_wide=d_wide, d_punch=d_punch,\
                            vrd_wide=vrd_wide, vrd_punch=vrd_punch, k_wide=k_wide, vrd_min_wide=vrd_min_wide,\
                            Ap2_wide=Ap2_wide, As_wide=As_wide, k_punch=k_punch, vrd_min_punch=vrd_min_punch,\
                            Ap2_punch=Ap2_punch, As_punch=As_punch, rho_final=rho_final, z=z, As_old=As_old,\
                            Asmin=Asmin, user=current_user)
        elif submit_type == 'advanced':
            # if user.is_authenticated:
                if b == 0:
                    return render_template('result.html', text="You", user=current_user)
                else:
                    return render_template('result_adv.html', b=b, d=d, As=As, N=N, s=s,\
                            qa=qa, fs=fs, qu=qu, dl=dl, ll=ll, mxp=mxp, mxv=mxv, myp=myp, myv=myv,\
                            col=col, coly=coly, cu=cu, df=df, gam=gam, fck=fck,\
                            fyk=fyk, bar=bar, cov=cov, p_s=p_s, ex=ex, ey=ey, sig_p=sig_p, D_wide=D_wide,\
                            D_punch=D_punch, ved_wide=ved_wide, ved_punch=ved_punch, vrd=vrd, med=med,\
                            mrd=mrd, rho_min=rho_min, SW_conc=SW_conc, SW_fill=SW_fill, B_final=B_final,\
                            D_final=D_final, d_final=d_final, sig_s=sig_s, d_wide=d_wide, d_punch=d_punch,\
                            vrd_wide=vrd_wide, vrd_punch=vrd_punch, k_wide=k_wide, vrd_min_wide=vrd_min_wide,\
                            Ap2_wide=Ap2_wide, As_wide=As_wide, k_punch=k_punch, vrd_min_punch=vrd_min_punch,\
                            Ap2_punch=Ap2_punch, As_punch=As_punch, rho_final=rho_final, z=z, As_old=As_old,\
                            Asmin=Asmin, user=current_user)
            # else:
            #     return redirect(url_for('auth.login'))
    return render_template('clay.html', user=current_user)


@views.route('/sand_soil_results', methods=['POST'])
def sand_soil_results():
    """ takes inputs and displays results for sand soil """
    dl = request.form['DL']
    ll = request.form['LL']
    mxp = request.form['mxp']
    mxv = request.form['mxv']
    myp = request.form['myp']
    myv = request.form['myv']
    col = request.form['COL']
    coly = request.form['COLY']
    phi = request.form['PHI']
    df = request.form['DF']
    gam = request.form['GAM']
    fck = request.form['FCK']
    fyk = request.form['FYK']
    bar = request.form['BAR']
    cov = request.form['COV']
    var_list = [dl, ll, mxp, mxv, myp, myv, col, coly, phi, df, gam, fck, fyk, bar, cov]
	
    def is_float(value):
        try:
            float(value)
            return True
        except ValueError:
            return False
	
    if any(not var for var in var_list):
        flash('An input field is blank.', category='error')
    elif any(not is_float(var) for var in var_list):    
        flash('An input field is not a number.', category='error')
    else:
        dl = float(request.form['DL'])
        ll = float(request.form['LL'])
        mxp = float(request.form['mxp'])
        mxv = float(request.form['mxv'])
        myp = float(request.form['myp'])
        myv = float(request.form['myv'])
        col = float(request.form['COL'])
        coly = float(request.form['COLY'])
        phi = float(request.form['PHI'])
        df = float(request.form['DF'])
        gam = float(request.form['GAM'])
        fck = float(request.form['FCK'])
        fyk = float(request.form['FYK'])
        bar = float(request.form['BAR'])
        cov = float(request.form['COV'])
        submit_type = request.form['submit_type']
        user = current_user
        b, d, As, N, s, qa, fs, qu, p_s, ex, ey, sig_p, D_wide, D_punch, ved_wide,\
            ved_punch, vrd, med, mrd, rho_min, SW_conc, SW_fill, B_final,\
            D_final, d_final, sig_s, d_wide, d_punch, vrd_wide, vrd_punch,\
            k_wide, vrd_min_wide, Ap2_wide, As_wide, k_punch, vrd_min_punch,\
            Ap2_punch, As_punch, rho_final, z, As_old, Asmin, Nc, Nq, Ngamma\
                = sand_iso(dl, ll, mxp, mxv, myp, myv, col, coly, phi, df, gam, fck, fyk, bar, cov)
        if submit_type == 'regular':
            if b == 0:
                return render_template('result.html', text="You", user=current_user)
            else:
                return render_template('result.html', b=b, d=d, As=As, N=N, s=s,\
                            qa=qa, fs=fs, qu=qu, dl=dl, ll=ll, mxp=mxp, mxv=mxv, myp=myp, myv=myv,\
                            col=col, coly=coly, phi=phi, df=df, gam=gam, fck=fck,\
                            fyk=fyk, bar=bar, cov=cov, p_s=p_s, ex=ex, ey=ey, sig_p=sig_p, D_wide=D_wide,\
                            D_punch=D_punch, ved_wide=ved_wide, ved_punch=ved_punch, vrd=vrd, med=med,\
                            mrd=mrd, rho_min=rho_min, SW_conc=SW_conc, SW_fill=SW_fill, B_final=B_final,\
                            D_final=D_final, d_final=d_final, sig_s=sig_s, d_wide=d_wide, d_punch=d_punch,\
                            vrd_wide=vrd_wide, vrd_punch=vrd_punch, k_wide=k_wide, vrd_min_wide=vrd_min_wide,\
                            Ap2_wide=Ap2_wide, As_wide=As_wide, k_punch=k_punch, vrd_min_punch=vrd_min_punch,\
                            Ap2_punch=Ap2_punch, As_punch=As_punch, rho_final=rho_final, z=z, As_old=As_old,\
                            Asmin=Asmin, Nc=Nc, Nq=Nq, Ngamma=Ngamma, user=current_user)
        elif submit_type == 'advanced':
            # if user.is_authenticated:
                if b == 0:
                    return render_template('result.html', text="You", user=current_user)
                else:
                    return render_template('result_adv.html', b=b, d=d, As=As, N=N, s=s,\
                            qa=qa, fs=fs, qu=qu, dl=dl, ll=ll, mxp=mxp, mxv=mxv, myp=myp, myv=myv,\
                            col=col, coly=coly, phi=phi, df=df, gam=gam, fck=fck,\
                            fyk=fyk, bar=bar, cov=cov, p_s=p_s, ex=ex, ey=ey, sig_p=sig_p, D_wide=D_wide,\
                            D_punch=D_punch, ved_wide=ved_wide, ved_punch=ved_punch, vrd=vrd, med=med,\
                            mrd=mrd, rho_min=rho_min, SW_conc=SW_conc, SW_fill=SW_fill, B_final=B_final,\
                            D_final=D_final, d_final=d_final, sig_s=sig_s, d_wide=d_wide, d_punch=d_punch,\
                            vrd_wide=vrd_wide, vrd_punch=vrd_punch, k_wide=k_wide, vrd_min_wide=vrd_min_wide,\
                            Ap2_wide=Ap2_wide, As_wide=As_wide, k_punch=k_punch, vrd_min_punch=vrd_min_punch,\
                            Ap2_punch=Ap2_punch, As_punch=As_punch, rho_final=rho_final, z=z, As_old=As_old,\
                            Asmin=Asmin, Nc=Nc, Nq=Nq, Ngamma=Ngamma, user=current_user)
            # else:
            #     return redirect(url_for('auth.login'))
    return render_template('sand.html', user=current_user)


@views.route('/bearing_cap_results', methods=['POST'])
def bearing_cap_results():
    """ takes inputs and displays results when bearing capacity is provided """
    dl = request.form['DL']
    ll = request.form['LL']
    mxp = request.form['mxp']
    mxv = request.form['mxv']
    myp = request.form['myp']
    myv = request.form['myv']
    col = request.form['COL']
    coly = request.form['COLY']
    bc = request.form['BC']
    fck = request.form['FCK']
    fyk = request.form['FYK']
    bar = request.form['BAR']
    cov = request.form['COV']
    var_list = [dl, ll, col, coly, mxp, mxv, myp, myv, bc, fck, fyk, bar, cov]
	
    def is_float(value):
        try:
            float(value)
            return True
        except ValueError:
            return False
	
    if any(not var for var in var_list):
        flash('An input field is blank.', category='error')
    elif any(not is_float(var) for var in var_list):    
        flash('An input field is not a number.', category='error')
    else:
        dl = float(request.form['DL'])
        ll = float(request.form['LL'])
        mxp = float(request.form['mxp'])
        mxv = float(request.form['mxv'])
        myp = float(request.form['myp'])
        myv = float(request.form['myv'])
        col = float(request.form['COL'])
        coly = float(request.form['COLY'])
        bc = float(request.form['BC'])
        fck = float(request.form['FCK'])
        fyk = float(request.form['FYK'])
        bar = float(request.form['BAR'])
        cov = float(request.form['COV'])
        submit_type = request.form['submit_type']
        user = current_user
        b, d, As, N, s, p_s, ex, ey, sig_p, D_wide, D_punch, ved_wide,\
            ved_punch, vrd, med, mrd, rho_min, SW_conc, SW_fill, B_final,\
            D_final, d_final, sig_s, d_wide, d_punch, vrd_wide, vrd_punch,\
            k_wide, vrd_min_wide, Ap2_wide, As_wide, k_punch, vrd_min_punch,\
            Ap2_punch, As_punch, rho_final, z, As_old, Asmin\
                = bearing_c_iso(dl, ll, mxp, mxv, myp, myv, col, coly, bc, fck, fyk, bar, cov)
        if submit_type == 'regular':
            if b == 0:
                return render_template('result.html', text="You", user=current_user)
            else:
                return render_template('result.html', b=b, d=d, As=As, N=N, s=s,\
                            dl=dl, ll=ll, mxp=mxp, mxv=mxv, myp=myp, myv=myv, col=col, coly=coly, bc=bc, fck=fck,\
                            fyk=fyk, bar=bar, cov=cov, p_s=p_s, ex=ex, ey=ey, sig_p=sig_p, D_wide=D_wide,\
                            D_punch=D_punch, ved_wide=ved_wide, ved_punch=ved_punch, vrd=vrd, med=med,\
                            mrd=mrd, rho_min=rho_min, SW_conc=SW_conc, SW_fill=SW_fill, B_final=B_final,\
                            D_final=D_final, d_final=d_final, sig_s=sig_s, d_wide=d_wide, d_punch=d_punch,\
                            vrd_wide=vrd_wide, vrd_punch=vrd_punch, k_wide=k_wide, vrd_min_wide=vrd_min_wide,\
                            Ap2_wide=Ap2_wide, As_wide=As_wide, k_punch=k_punch, vrd_min_punch=vrd_min_punch,\
                            Ap2_punch=Ap2_punch, As_punch=As_punch, rho_final=rho_final, z=z, As_old=As_old,\
                            Asmin=Asmin, user=current_user)
        elif submit_type == 'advanced':
            # if user.is_authenticated:
                if b == 0:
                    return render_template('result.html', text="You", user=current_user)
                else:
                    return render_template('result_adv.html',b=b, d=d, As=As, N=N, s=s,\
                            dl=dl, ll=ll, mxp=mxp, mxv=mxv, myp=myp, myv=myv, col=col, coly=coly, bc=bc, fck=fck,\
                            fyk=fyk, bar=bar, cov=cov, p_s=p_s, ex=ex, ey=ey, sig_p=sig_p, D_wide=D_wide,\
                            D_punch=D_punch, ved_wide=ved_wide, ved_punch=ved_punch, vrd=vrd, med=med,\
                            mrd=mrd, rho_min=rho_min, SW_conc=SW_conc, SW_fill=SW_fill, B_final=B_final,\
                            D_final=D_final, d_final=d_final, sig_s=sig_s, d_wide=d_wide, d_punch=d_punch,\
                            vrd_wide=vrd_wide, vrd_punch=vrd_punch, k_wide=k_wide, vrd_min_wide=vrd_min_wide,\
                            Ap2_wide=Ap2_wide, As_wide=As_wide, k_punch=k_punch, vrd_min_punch=vrd_min_punch,\
                            Ap2_punch=Ap2_punch, As_punch=As_punch, rho_final=rho_final, z=z, As_old=As_old,\
                            Asmin=Asmin, user=current_user)
            # else:
            #     return redirect(url_for('auth.login'))
    return render_template('bearing_c.html', user=current_user)
    

@views.route('/save', methods=['GET', 'POST'])
@login_required
def save():
    """ saves users advanced results """
    if request.method == 'POST': 
        note = request.form.get('note')#Gets the note from the HTML 

        if len(note) < 1:
            flash('Note is too short!', category='error') 
        else:
            new_note = Note(data=note, user_id=current_user.id)  #providing the schema for the note 
            db.session.add(new_note) #adding the note to the database 
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("saved.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    """ deletes the saved advanced results """
    note = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})
