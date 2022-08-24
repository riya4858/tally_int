import datetime
from datetime import timedelta
from django.contrib import messages
from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def index(request):
    comp=Companies.objects.all()
    return render(request,'index.html',{'comp':comp})
def base(request):
    comp=Companies.objects.all()
    return render(request,'base.html',{'comp':comp})

def featurepage(request):
    comp=Companies.objects.all()
    return render(request,'featurepage.html',{'comp':comp})
#......................jisha........................

def company_list(request):
    com=Companies.objects.all()
    return render(request,'company_list.html',{'comp':com})    

def change_company(request):
	com=Companies.objects.all()
	return render(request, 'change_company.html',{'comp':com})

def select_c(request):
	com = Companies.objects.all()
	return render(request,'select_c.html',{'com':com})

def shut_cmpny(request):
	com=Companies.objects.all() 
	return render(request, 'shut_cmpny.html',{'com':com})

def shut(request,pk):
    c=Companies.objects.get(id=pk)
    c.status=False
    c.save()
    return redirect('shut_cmpny') 

def enable(request,pk):
    c=Companies.objects.get(id=pk)
    c.status=True
    c.save()
    return redirect('/')

def ledgers(request,pk):
	grp=tally_group.objects.all()
	com=Companies.objects.get(id=pk) 
	return render(request,'ledgers.html',{'grp' : grp,'cmp':com})

def vouchers(request,pk):
	com=Companies.objects.get(id=pk) 
	return render(request, 'vouchers.html',{'cmp':com})



def currency(request,pk):
    cmp=Companies.objects.get(id=pk)
    return render(request, 'currency.html',{'cmp':cmp})

def c_create(request,pk):
    cmp=Companies.objects.get(id=pk)
    return render(request, 'c_create.html',{'cmp':cmp})

def c_alter(request,pk):
    cmp=Companies.objects.get(id=pk)
    return render(request, 'c_alter.html',{'cmp':cmp})

def costcentre(request,pk):
    cmp=Companies.objects.get(id=pk)
    if request.method == 'POST':
        cmp=Companies.objects.get(id=pk)
        cname = request.POST['cname']
        alia = request.POST['alia']
        under = request.POST['under']
        costc=cost_centre.objects.filter(cname=cname)
        if costc:
            # messages.info(request,'Company name already exists!!')
            pass
        else:
            
            data = cost_centre(cname=cname,cost_alias=alia,under=under,company=cmp)
            data.save()
            return redirect('index')
    ccentre=cost_centre.objects.filter(company_id=cmp)
    return render(request,'costcentre.html',{'cmp':cmp,'ccentre':ccentre})

def costcentre2(request,pk):
    cmp=Companies.objects.get(id=pk)
    if request.method == 'POST':
        cmp=Companies.objects.get(id=pk)
        cname = request.POST['cname']
        alia = request.POST['alia']
        under = request.POST['under']
        costc=cost_centre.objects.filter(cname=cname)
        if costc:
            # messages.info(request,'Company name already exists!!')
            pass
        else:
            
            data = cost_centre(cname=cname,cost_alias=alia,under=under,company=cmp)
            data.save()
            return redirect('index')
    ccentre=cost_centre.objects.filter(company_id=cmp)
    return render(request,'costcentre2.html',{'cmp':cmp,'ccentre':ccentre})


def ratesofexchange(request,pk):
    cmp=Companies.objects.get(id=pk)
    if request.method == 'POST':
        cmp=Companies.objects.get(id=pk)
        
        currencyName = request.POST['cr']
        stdrate = request.POST['stdrate']
        # sell_voucher_rate = request.POST['sell_voucher_rate']
        sell_specified_rate = request.POST['sell_specified_rate']
        # buy_voucher_rate = request.POST['buy_voucher_rate']
        buy_specified_rate = request.POST['buy_specified_rate']
        mdl = rateofexchange(
            currencyName=currencyName,
            stdrate=stdrate,
            # sell_voucher_rate=sell_voucher_rate,
            sell_specified_rate=sell_specified_rate,
            # buy_voucher_rate=buy_voucher_rate,
            buy_specified_rate=buy_specified_rate,
            company = cmp)
        mdl.save()
        return redirect('index')
    cur=currencyAlteration.objects.filter(company_id=cmp)
    return render(request,'ratesofexchange.html',{'cmp':cmp,'curr':cur})


def create_cmpny(request):
    return render(request, 'create_cmpny.html')

def tally_gst(request,pk):
	company=Companies.objects.get(id=pk)
	return render(request, 'gst.html',{'company':company})

def gst_tax(request,pk):
	company=Companies.objects.get(id=pk)
	return render(request, 'gst_tax.html',{'company':company})

def features(request):
	return render(request, 'features.html')

def tds(request,pk):
	comp=Companies.objects.get(id=pk)
	return render(request, 'tds.html',{'company':comp})    

def person(request,pk):
	comp=Companies.objects.get(id=pk)
	return render(request, 'tds_person.html',{'company':comp})
    
def c_rates(request):
    return render(request, 'c_rates.html')

def bank_details(request):
	bn = bank_name.objects.all()
	return render(request,'bank_details.html',{'bn' : bn})

def lut_bond(request):
    return render(request, 'lut_bond.html')

def cheque(request):
    return render(request, 'cheque.html')

def ledger_gst(request):
    return render(request, 'ledger_gst.html')

def ledger_chequed(request):
    return render(request, 'ledger_chequed.html')

def vouch_advance(request,pk):
    cmp=Companies.objects.get(id=pk)
    return render(request, 'vouch_advance.html',{'cmp':cmp})

def ledger_taxgst(request):
    return render(request, 'ledger_taxgst.html')

def b_name(request):
	comp=Companies.objects.all()
	return render(request,'bankname.html',{'comp':comp})

def groups(request,pk):
    cmp=Companies.objects.get(id=pk)
    if request.method == 'POST':
        cmp=Companies.objects.get(id=pk)
        gname = request.POST['gname']
        alia = request.POST['alia']
        under = request.POST['under']
        sub_ledger = request.POST['sub_ledger']
        gross = request.POST['gross']
        nett = request.POST['nee']
        calc = request.POST['cal']
        meth = request.POST['meth']
        nature = request.POST['nature']
        grp=tally_group.objects.filter(group_name=gname)
        if grp:
            # messages.info(request,'Company name already exists!!')
            pass
        else:
            mdl = tally_group(
                group_name=gname,
                group_alias=alia,
                group_under=under,
                sub_ledger=sub_ledger,
                debit_credit=nett,
                calculation=calc,
                invoice=meth,
                nature=nature,
                gross_profit=gross,
                company=cmp
            )
            mdl.save()
            return redirect('index')
    grup=tally_group.objects.filter(company_id=cmp)
    return render(request,'group.html',{'cmp':cmp,'grup':grup})
    
def group2(request,pk):
    cmp=Companies.objects.get(id=pk)
    if request.method == 'POST':
        cmp=Companies.objects.get(id=pk)
        gname = request.POST['gname']
        alia = request.POST['alia']
        under = request.POST['under']
        sub_ledger = request.POST['sub_ledger']
        gross = request.POST['gross']
        nett = request.POST['nee']
        calc = request.POST['cal']
        meth = request.POST['meth']
        nature = request.POST['nature']
        grp=tally_group.objects.filter(name=gname)
        if grp:
            # messages.info(request,'Company name already exists!!')
            pass
        else:
            mdl = tally_group(
                group_name=gname,
                group_alias=alia,
                group_under=under,
                sub_ledger=sub_ledger,
                debit_credit=nett,
                calculation=calc,
                invoice=meth,
                nature=nature,
                gross_profit=gross,
                company=cmp
            )
            mdl.save()
            return redirect('index')
    grup=tally_group.objects.filter(company_id=cmp)
    return render(request,'group2.html',{'cmp':cmp,'grup':grup})
def create_currency(request,pk):
	if request.method=='POST':
		cmp=Companies.objects.get(id=pk)
		smbl=request.POST['c_symbl']
		fname=request.POST['fname']
		isoc=request.POST['isocode']
		dcml=request.POST['decimal_p']
		amt=request.POST['show_amt']
		sfx=request.POST['suffix']
		spc=request.POST['add_space']
		wrd=request.POST['word_rep']
		ndcml=request.POST['no_decimal']
		crny=currencyAlteration(Symbol=smbl,
                        FormalName = fname,
                        ISOCurrency = isoc,
                        DecimalPlace = dcml,
                        showAmount = amt,
                        suffixSymbol = sfx,
                        AddSpace = spc,
                        wordRep = wrd,
                        DecimalWords = ndcml,company=cmp)          
		crny.save()
		print("added")
		return redirect('/')
def company(request):
    com=Companies.objects.all()
    return render(request,'company.html',{'com':com})

def altercompanyview(request):
    com=Companies.objects.all()
    return render(request,'altercompanyview.html',{'com':com})

def altercompany(request,pk):
    comp=Companies.objects.get(id=pk)
    if request.method == 'POST':
        comp.name=request.POST['companyname']
        comp.mailing_name=request.POST['mailing_name']
        comp.address=request.POST['address']
        
        comp.state=request.POST['state']
        comp.country=request.POST['country']
        
        comp.pincode=request.POST['pincode']
        comp.telephone=request.POST['telephone']
        comp.mobile=request.POST['mobile']
        comp.fax=request.POST['fax']
        comp.email=request.POST['email']
        comp.website=request.POST['website']
        comp.fin_begin=request.POST['fyear']
        comp.books_begin=request.POST['byear']
        comp.currency_symbol=request.POST['currency']
        comp.formal_name=request.POST['formal']
        comp.save()
        return redirect('company')
    return render(request,'editcompany.html',{'comp':comp})

def selectcompany(request):
    com=Companies.objects.all()
    return render(request,'selectcompany.html',{'com':com})

def shutcompany(request):
    com=Companies.objects.all()
    return render(request,'shutcompany.html',{'com':com})

def disable(request,pk):
    c=Companies.objects.get(id=pk)
    c.status=False
    c.save()
    return redirect('shutcompany')

def altercompany(request,pk):
    
    comp=Companies.objects.get(id=pk)
    if request.method == 'POST':
        comp.name=request.POST['name']
        comp.mailing_name=request.POST['mailing_name']
        comp.address=request.POST['address']
        
        comp.states=request.POST['state']
        comp.country=request.POST['country']
        
        comp.pincode=request.POST['pincode']
        comp.telephone=request.POST['telephone']
        comp.mobile=request.POST['mobile']
        comp.fax=request.POST['fax']
        comp.email=request.POST['email']
        comp.website=request.POST['website']
        comp.fin_begin=request.POST['fin_begin']
        comp.books_begin=request.POST['books_begin']
        comp.currency_symbol=request.POST['currency_symbol']
        comp.formal_name=request.POST['formal_name']
        comp.save()
        return redirect('altercompanyview')
    return render(request,'editcompany.html',{'comp':comp})
def enable(request,pk):
    c=Companies.objects.get(id=pk)
    c.status=True
    c.save()
    return redirect('shutcompany')

def ratesofexchange(request,pk):
    cmp=Companies.objects.get(id=pk)
    curcc=currencyAlteration.objects.all()
    return render(request,'ratesofexchange.html',{'cmp':cmp,'cur':curcc})

def create_ROE(request,pk):
	if request.method=='POST':
		cmp=Companies.objects.get(id=pk)
		dt=request.POST['dt']
		crname=request.POST['curname']
		stdr=request.POST['stdr']
		lv=request.POST['lvr']
		ssr=request.POST['ssr']
		lv1=request.POST['lvr2']
		bsr=request.POST['bsr']
		croe=rateofexchange(date_ROE=dt,
                        currencyName = crname,
                        std_rate = stdr,
                        sell_voucher_rate = lv,
                        sell_specified_rate = ssr,
						buy_specified_rate = lv1,
                        buy_voucher_rate = bsr,company=cmp)          
		croe.save()
		return redirect('/')

def alter_currency(request,pk):
	if request.method=='POST':
		cmp=Companies.objects.get(id=pk)
		smbl=request.POST['c_symbl']
		fname=request.POST['fname']
		isoc=request.POST['isocode']
		dcml=request.POST['decimal_p']
		amt=request.POST['show_amt']
		sfx=request.POST['suffix']
		spc=request.POST['add_space']
		wrd=request.POST['word_rep']
		ndcml=request.POST['no_decimal']
		crny=company_alt_currency(c_symbol=smbl,
                        formal_name = fname,
                        iso_Ccode = isoc,
                        decimal_place = dcml,
                        show_amtM = amt,
                        suffix_smblA = sfx,
                        add_space = spc,
                        word_rep = wrd,
                        no_decimal = ndcml,company=cmp)          
		crny.save()
		print("added")
		return redirect('/')

def load_centre(request):
	if request.method=='POST':
		nm=request.POST['cst_name']
		als=request.POST['alias']
		unr=request.POST['c_under']
		cost=cost_centre(cname=nm,
                        cost_alias = als,
                        under = unr)          
		cost.save()
		print("added")
		return render(request,'cost.html')
		

def create_tds(request,pk):
	id=Companies.objects.get(id=pk)
	if request.method=='POST':
		t_reg = request.POST['tan_reg_no']
		tax_clct = request.POST['tax_ded_clctn']
		ded_type = request.POST['deductor_type']
		ded_bd = request.POST['ded_brachdevision']
		prsn_res = request.POST['person_res']
		ignr = request.POST['ignore_it']
		st_itm = request.POST['tds_stock_items']
		
		ctds=Tds_Details(tan_regno=t_reg,
                        tan = tax_clct,
                        deductor_type = ded_type,
                        deductor_branch = ded_bd,
                        person_details = prsn_res,
                        ignore_it = ignr,
                        active_tds = st_itm,
						company = id)          
		ctds.save()
		print("added")
		return redirect('/')
	return render(request,'tds.html')

def person_tds(request,pk):
	id=Companies.objects.get(id=pk)
	if request.method=='POST':
		name = request.POST['name']
		sd = request.POST['son_daughter']
		des = request.POST['designation']
		pan = request.POST['pan']
		ftno = request.POST['flat_no']
		pnm = request.POST['premise_name']
		str = request.POST['street']
		are = request.POST['area']
		city = request.POST['city']
		st = request.POST['state']
		pcd = request.POST['pincode']
		m_no = request.POST['mobile_no']
		std = request.POST['std_code']
		tph = request.POST['telephone']
		emal = request.POST['email']
	    
		prs=tds_person(name=name,
                        son_daughter = sd,
                        designation = des,
                        pan = pan,
                        flat_no = ftno,
                        building = pnm,
                        street = str,
                        area = are,
                        town = city,
                        state = st,
                        pincode = pcd,
                        mobile = m_no,
                        std = std,
                        telephone = tph,
                        email = emal,
						company = id)          
		prs.save()
		print("added")
		return redirect('/')
	return render(request,'tds_person.html')

def create_voucher(request,pk):
	if request.method=='POST':
		cmp=Companies.objects.get(id=pk)
     
		nm=request.POST['vname']
		als=request.POST['alias']
		vtp=request.POST['vouch_type']
		abbr=request.POST['Abbreviation']
		actp=request.POST['activate_Vtype']
		mvno=request.POST['method_Vno']
		prnt=request.POST['prevent']
		acn=request.POST['advance_con']
		use=request.POST['use_EDV']
		zero=request.POST['zero_val']
		mvd=request.POST['mVoptional_defualt']
		anar=request.POST['allow_nar']
		prvdl=request.POST['provide_L']
		jrnl=request.POST['manu_jrnl']
		track=request.POST['track_purchase']
		enbl=request.POST['enable_acc']
		prntva=request.POST['prnt_VA_save']
		prntfml=request.POST['prnt_frml']
		juri=request.POST['jurisdiction']
		tprint=request.POST['title_print']
		setaltr=request.POST['set_alter']
		posinv=request.POST['pos_invoice']
		msg1=request.POST['msg_1']
		msg2=request.POST['msg_2']
		dbank=request.POST['default_bank']
		nc=request.POST['name_class']

		vhr=Voucher(voucher_name=nm,
                    alias = als,
                    voucher_type = vtp,
                    abbreviation = abbr,
                    voucherActivate = actp,
                    voucherNumber = mvno,
                    preventDuplicate = prnt,
                    advance_con = acn,
                    voucherEffective = use,
                    transaction = zero,
                    make_optional = mvd,
                    voucherNarration = anar,
                    provideNarration = prvdl,
                    manu_jrnl = jrnl,
                    track_purchase = track,
                    enable_acc = enbl,
                    prnt_VA_save = prntva,
                    prnt_frml = prntfml,
                    jurisdiction = juri,
                    title_print = tprint,
                    set_alter = setaltr,
                    pos_invoice = posinv,
                    msg_1 = msg1,
                    msg_2 = msg2,
                    default_bank = dbank,
                    name_class = nc,
                    company=cmp)          
		vhr.save()
		print("Added")
		return redirect('/')



def create_gst(request,pk):
	id=Companies.objects.get(id=pk)
	if request.method=='POST':
		st = request.POST['state']
		rt = request.POST['registration_type']
		at = request.POST['assessee_territory']
		gsta = request.POST['gst_applicable']
		gstuin = request.POST['gstin_uin']
		prd = request.POST['periodicity']

	# .................regular.................

		kfca = request.POST['kerala_fca']
		af = request.POST['applicable_from']
		gstrd = request.POST['gst_rate_details']
		tla = request.POST['tl_advanceR']
		tlr = request.POST['tl_reverseC']
		gstc = request.POST['gst_classification'] 
		lb = request.POST['lut_bond']

    # ................composition................  
	  
		tr = request.POST['tax_rate']
		tc = request.POST['tax_calculation']
		tp = request.POST['tax_purchase']

	# ............e-Way bill applicable...........

		ea = request.POST['e_waybillA']
		aaf = request.POST['applicable_f']
		tli = request.POST['thresholdlimit_include']
		tl = request.POST['threshold_limit']
		intr = request.POST['intrastate']
		itl = request.POST['ithreshold_limit']
		pnw = request.POST['print_eway']

	# .............e-Invoice applicable..............

		einva = request.POST['e_invoiceA']
		appf = request.POST['app_f']
		bfp = request.POST['billfrom_place']
		peir = request.POST['period_einvoiceR']
		sewdei = request.POST['send_eW_details_einvoice']
        
		gstd=GST(state=st,
						reg_type=rt,
						assessee=at,
						gst_applicable=gsta,
						gstin=gstuin,
						periodicity=prd,
					# ........regular.......
						flood_cess=kfca,
						applicable_from=af,
						gst_rate_details=gstrd,
						advance_receipts=tla,
						reverse_charge=tlr,
						gst_classification=gstc,
						bond_details=lb,	
					# ........composition.......
						tax_rate=tr,		
						tax_calc=tc,		
						tax_purchase=tp,
					# ........e-Way bill applicable.......
						eway_bill=ea,
						applicable_form=aaf,
						threshold_includes=tli,
						threshold_limit=tl,
						intrastate=intr,
						threshold_limit2=itl,
						print_eway=pnw,
					# ........e-Invoice applicable.......
						e_invoice=einva,
						app_from=appf,
						billfrom_place=bfp,
						dperiod=peir,
						send_ewaybill=sewdei,
						company=id)
		gstd.save()
		print("Added")
		return redirect('/')
	return render(request,'gst.html')

def create_gsttax(request,pk):
	id=Companies.objects.get(id=pk)
	if request.method=='POST':
		txb=request.POST['taxability']
		af=request.POST['appicable_from']
		it=request.POST['integrated_tax']
		ces=request.POST['cess']
		fc=request.POST['flood_cess']
		
		cost=gst_taxability(taxability=txb,
                        applicable_dt = af,
                        integrated_tax = it,      
                        cess = ces,      
                        flood_cess = fc,
						company = id)          
		cost.save()
		print("Added")
		return redirect('/')
	return render(request,'gst_tax.html')

def create_lutbond(request):
	if request.method=='POST':
		lbno=request.POST['lut_bondNo']
		afrom=request.POST['application_from']
		ato=request.POST['application_to']
		lb=gst_lutbond(lutbond=lbno,
                        validity_from = afrom,
                        validity_to = ato)      
		lb.save() 
		print("Added")
		return redirect('lut_bond')
	return render(request,'lut_bond')

def create_ledger(request,pk):
    cmp=Companies.objects.get(id=pk)
    if request.method=='POST':
        cmp=Companies.objects.get(id=pk)
        nm=request.POST.get('name')
        als=request.POST.get('alias')
        under=request.POST.get('under')
        mname=request.POST.get('mailingname')
        adr=request.POST.get('address')
        st=request.POST.get('state')
        cntry=request.POST.get('country')
        pin=request.POST.get('pincode')
        pno=request.POST.get('pan_no')
        bdetls=request.POST.get('bank_details')
        rtype=request.POST.get('registration_type')
        gst_uin=request.POST.get('gst_uin')
        opnbn=request.POST.get('opening_blnc')

        spdl=request.POST.get('set_odl')
        achnm=request.POST.get('ac_holder_nm')
        acno=request.POST.get('acc_no')
        ifsc=request.POST.get('ifsc_code')
        scode=request.POST.get('swift_code')
        bn=request.POST.get('bank_name')
        brnch=request.POST.get('branch')
        sacbk=request.POST.get('SA_cheque_bk')
        ecp=request.POST.get('Echeque_p')
        sacpc=request.POST.get('SA_chequeP_con')

        typofled=request.POST.get('type_of_ledger')
        rometh=request.POST.get('rounding_method')
        rolmt=request.POST.get('rounding_limit')

        typdutytax=request.POST.get('type_duty_tax')
        taxtyp=request.POST.get('tax_type')
        valtype=request.POST.get('valuation_type')
        rateperu=request.POST.get('rate_per_unit')
        percalc=request.POST.get('percentage_of_calcution')
        rondmethod=request.POST.get('rond_method')
        roimlit=request.POST.get('rond_limit')

        gstapplicbl=request.POST.get('gst_applicable')
        sagatdet=request.POST.get('setalter_gstdetails')
        typsupply=request.POST.get('type_of_supply')
        asseval=request.POST.get('assessable_value')
        appropto=request.POST.get('appropriate_to')
        methcalcu=request.POST.get('method_of_calculation')

        balbillbybill=request.POST.get('balance_billbybill')
        credperiod=request.POST.get('credit_period')
        creditdaysvouch=request.POST.get('creditdays_voucher')
        
        ldr=tally_ledger(name=nm,alias=als,under=under,mname=mname,address=adr,state=st,country=cntry,
						pincode=pin,pan_no=pno,bank_details=bdetls,registration_type=rtype,gst_uin=gst_uin,
						opening_blnc=opnbn,set_odl=spdl,ac_holder_nm=achnm,acc_no=acno,ifsc_code=ifsc,swift_code=scode,
						bank_name=bn,branch=brnch,SA_cheque_bk=sacbk,Echeque_p=ecp,SA_chequeP_con=sacpc,
						type_of_ledger=typofled,rounding_method=rometh,rounding_limit=rolmt,type_duty_tax=typdutytax,tax_type=taxtyp,
						valuation_type=valtype,rate_per_unit=rateperu,percentage_of_calcution=percalc,rond_method=rondmethod,rond_limit=roimlit,
						gst_applicable=gstapplicbl,setalter_gstdetails=sagatdet,type_of_supply=typsupply,assessable_value=asseval,
						appropriate_to=appropto,method_of_calculation=methcalcu,balance_billbybill=balbillbybill,credit_period=credperiod,
						creditdays_voucher=creditdaysvouch,company=cmp)
		
        ldr.save()
        return redirect('/')
        

def create_ledgerdimension(request,pk):
   
	if request.method == 'POST':
		cmp=Companies.objects.get(id=pk)
		cw= request.POST.get('cheque_width')
		ch= request.POST.get('cheque_height')
		sle= request.POST.get('startL_leftEdge')
		slte= request.POST.get('startL_topEdge')
		dlle= request.POST.get('distancel_leftEdge')
		dlte= request.POST.get('distancel_topEdge')
		ds= request.POST.get('date_style')
		dts= request.POST.get('date_seperator')
		sw= request.POST.get('separator_width')
		cd= request.POST.get('character_distance')
		pdle= request.POST.get('Pdistancel_leftEdge')
		pdlte= request.POST.get('Pdistancel_topEdge')
		aw= request.POST.get('area_width')
		sldte= request.POST.get('secondL_DTE')
		sflh= request.POST.get('secondfirstL_height')
		fldte= request.POST.get('firstL_dTE')
		slfle= request.POST.get('sl_fisrtl_LE')
		slsle= request.POST.get('sl_secondl_LE')
		awa= request.POST.get('amount_widtharea')
		cfnmp= request.POST.get('currencyFNM_print')
		dfte= request.POST.get('df_TE')
		sle= request.POST.get('startL_LE')
		amwa= request.POST.get('amt_widtharea')
		csp= request.POST.get('currencyS_print')
		cn= request.POST.get('company_name')
		pcn= request.POST.get('print_CN')
		sfs= request.POST.get('salutation_Fsign')
		sss= request.POST.get('salutation_Ssign')
		tes= request.POST.get('top_Edistance')
		slfl= request.POST.get('startLF_leftE')
		wsa= request.POST.get('width_sign_area')
		hsa= request.POST.get('height_sign_area')

		cld= ledger_cheque_demension(cheque_width=cw,cheque_height=ch,startL_leftEdge=sle,startL_topEdge=slte,distancel_leftEdge=dlle,
									distancel_topEdge=dlte,date_style=ds,date_seperator=dts,separator_width=sw,character_distance=cd,
									Pdistancel_leftEdge=pdle,Pdistancel_topEdge=pdlte,area_width=aw,secondL_DTE=sldte,secondfirstL_height=sflh,
									firstL_dTE=fldte,sl_fisrtl_LE=slfle,sl_secondl_LE=slsle,amount_widtharea=awa,currencyFNM_print=cfnmp,
									df_TE=dfte,startL_LE=sle,amt_widtharea=amwa,currencyS_print=csp,company_name=cn,print_CN=pcn,
									salutation_Fsign=sfs,salutation_Ssign=sss,top_Edistance=tes,startLF_leftE=slfl,width_sign_area=wsa,
									height_sign_area=hsa,company=cmp)

		cld.save()
		return redirect('/')
	return render(request,'ledger_chequed.html')

def company_create(request):
	if request.method=="POST":
		name=request.POST['companyname']
		mname=request.POST['mailing_name']
		addr=request.POST['address']
		st=request.POST['state']
		cntry=request.POST['country']
		pncd=request.POST['pincode']
		tlphn=request.POST['telephone']
		mbl=request.POST['mobile']
		fax=request.POST['fax']
		email=request.POST['email']
		wbsit=request.POST['website']
		fin_begin=request.POST['fyear']
		bk_begin=request.POST['byear']
		crny_symbol=request.POST['currency']
		frml_name=request.POST['formal']

		ccmp=Companies.objects.filter(name=name)
		out=datetime.datetime.strptime (fin_begin,'%Y-%m-%d')+timedelta (days=364) 
		a=out.date()
		

		if ccmp:
			messages.info(request,'Company name already exists!!')
			return redirect('create_cmpny')
		else:
			cmp=Companies(name=name,mailing_name=mname,address=addr,state=st,country=cntry,
                pincode=pncd,telephone=tlphn,mobile=mbl,fax=fax,email=email,website=wbsit,fin_begin=fin_begin,
                books_begin=bk_begin,currency_symbol=crny_symbol,formal_name=frml_name,fin_end=a)
			cmp.save()
			messages.info(request,'Company created successfully(Enable the features as per your business needs)')
			return render(request,'features.html',{'cmp':cmp})

def company_feature(request,cf):
	id=Companies.objects.get(id=cf)
	if request.method=="POST":
		ma=request.POST['maintain_account']
		be=request.POST['billwise_entry']
		cc=request.POST['cost_centre']
		ic=request.POST['interest_calculation']
		mi=request.POST['maintain_inventry']
		ai=request.POST['account_inventry']
		mpl=request.POST['multiple_pricelevel']
		eb=request.POST['enable_batches']
		edt=request.POST['expiry_date']
		jop=request.POST['job_order_procress']
		ct=request.POST['cost_tracking']
		jc=request.POST['job_costing']
		dc=request.POST['discount_column']
		sa=request.POST['seperte_actual']
		gst=request.POST['gst']
		tds=request.POST['tds']
		tcs=request.POST['tcs']
		vat=request.POST['vat']
		excise=request.POST['excise']
		st=request.POST['service_tax']
		prl=request.POST['payroll']
		maddr=request.POST['multiple_address']
		mark_mod=request.POST['mark_modified']

		cmp_fet=Features(maintain_accounts=ma,bill_wise_entry=be,cost_centres=cc,interest_calc=ic,maintain_inventory=mi,
		integrate_accounts=ai,multiple_price_level=mpl,batches=eb,expirydate_batches=edt,joborder_processing=jop,cost_tracking=ct,job_costing=jc,discount_invoices=dc,
		Billed_Quantity=sa,gst=gst,tds=tds,tcs=tcs,vat=vat,excise=excise,servicetax=st,payroll=prl,multiple_addrss=maddr,
		vouchers=mark_mod,company=id)

		cmp_fet.save()
		return redirect('/')
	return render(request,'features.html',{'cmp':id})

def create_bankdetails(request,pk):
	if request.method=='POST':
		cmp=Companies.objects.get(id=pk)
     
		transaction_type=request.POST['transaction_type']
		acp=request.POST['ac_payee']
		acc_no=request.POST['acc_no']
		ifsc_code=request.POST['ifsc_code']
		bank_name=request.POST['bank_name']
		lbd=ledger_bankdetails(transaction_type=transaction_type,
                        cross_using = acp,
                        acc_no = acc_no,      
                        ifsc_code = ifsc_code,      
                        bank_name =bank_name,company=cmp)      
		lbd.save() 
		print("Added")
		return redirect('bank_details')
	return render(request,'bank_details.html')


def bankname(request,pk):
	if request.method=='POST':
		cmp=Companies.objects.get(id=pk)
		bn = request.POST['bank_name']
		bnn=bank_name(bankname = bn,company=cmp)
		bnn.save()
		return redirect('bankname')
	return render(request,'bankname.html')


def create_chequebk(request,pk):
	if request.method=='POST':
		cmp=Companies.objects.get(id=pk)
		fn=request.POST['from_number']
		tn=request.POST['to_number']
		nc=request.POST['number_cheques']
		nmc=request.POST['name_chequebk']
		lcb=ledger_chequebook(from_number=fn,
                        to_number = tn,
                        no_of_cheques = nc,
                        cheque_bookname = nmc,company=cmp)      
		lcb.save() 
		print("Added")
		return redirect('cheque')
	return render(request,'cheque.html')

def create_ledger_gst(request,pk):
	if request.method=='POST':
		cmp=Companies.objects.get(id=pk)
		ntrot=request.POST['nature_of_transaction']
		txbl=request.POST['taxable']
		txblty=request.POST['taxability']
		aplifm=request.POST['appicable_from']
		inttx=request.POST['integrated_tax']
		ces=request.POST['cess']
		lgst=ledger_gstvalues(nature_of_transaction=ntrot,
                        taxable = txbl,
                        taxability = txblty,
                        appicable_from = aplifm,
                        integrated_tax = inttx,
                        cess = ces,company=cmp)    
		lgst.save()  
		print("Added")
		return redirect('ledger_gst')
	return render(request,'ledger_gst.html')

def create_voucher_advance(request,pk):
	if request.method=='POST':
		cmp=Companies.objects.get(id=pk)
		stn=request.POST['starting_no']
		npw=request.POST['numerical_partwidth']
		pz=request.POST['prefill_zero']
		rsad=request.POST['restart_applicable_dt']
		rsrtsno=request.POST['restart_startingno']
		repert=request.POST['restart_particular']
		pread=request.POST['prefix_applicable_dt']
		preper=request.POST['prefix_particular']
		sfxapd=request.POST['suffix_applicable_dt']
		sfxper=request.POST['suffix_particular']

		cva=voucher_advanceconf(starting_no=stn,
                        numerical_partwidth = npw,
                        prefill_zero = pz,
                        restart_applicable_dt = rsad,
                        restart_startingno = rsrtsno,
                        restart_particular = repert,
                        prefix_applicable_dt = pread,
                        prefix_particular = preper,
                        suffix_applicable_dt = sfxapd,
                        suffix_particular = sfxper,company=cmp)    
		cva.save()  
		print("Added")
		return redirect('vouch_advance')
	return render(request,'vouch_advance.html')

def create_ledger_taxgst(request,pk):
	if request.method=='POST':
		cmp=Companies.objects.get(id=pk)
		regtp=request.POST['registration_type']
		assester=request.POST['assessee_teritory']
		comop=request.POST['commerce_operator']
		partde=request.POST['party_deemed']
		partytyp=request.POST['party_type']
		gstinuin=request.POST['gstin_uin']
		transp=request.POST['transporter']
		transpid=request.POST['transporter_id']

		lgt=ledger_taxreggst(registration_type=regtp,
                        assessee_teritory = assester,
                        commerce_operator = comop,
                        party_deemed = partde,
                        party_type = partytyp,
                        gstin_uin = gstinuin,
                        transporter = transp,
                        transporter_id = transpid,company=cmp)    
		lgt.save()  
		print("Added")
		return redirect('ledger_taxgst')
	return render(request,'ledger_taxgst.html')

