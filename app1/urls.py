from django.urls import path
from.import views


urlpatterns = [

    path('',views.index,name='index'),
    path('base',views.base,name='base'),
    path('featurepage',views.featurepage,name='featurepage'),

#.........................jisha..........................
    

    path('ledgers/<int:pk>',views.ledgers,name='ledgers'),

    path('vouchers/<int:pk>',views.vouchers,name='vouchers'),

    path('groups/<int:pk>',views.groups,name='groups'),
    path('group2/<int:pk>',views.group2,name='group2'),
    path('ratesofexchange/<int:pk>',views.ratesofexchange,name='ratesofexchange'),



    path('currency/<int:pk>',views.currency,name='currency'),

    path('c_create/<int:pk>',views.c_create,name='c_create'),

    path('c_alter/<int:pk>',views.c_alter,name='c_alter'),

    path('costcentre/<int:pk>',views.costcentre,name='costcentre'),
    path('costcentre2/<int:pk>',views.costcentre2,name='costcentre2'),
    

    path('change_company',views.change_company,name='change_company'),

    path('company_list',views.company_list,name='company_list'),

    path('select_c',views.select_c,name='select_c'),

    path('create_cmpny',views.create_cmpny,name='create_cmpny'),
    
    path('features',views.features,name='features'),

    path('tally_gst/<int:pk>',views.tally_gst,name='tally_gst'),

    path('create_gst/<int:pk>',views.create_gst,name='create_gst'),

    path('gst_tax/<int:pk>',views.gst_tax,name='gst_tax'),

    path('lut_bond',views.lut_bond,name='lut_bond'),

    path('create_gsttax/<int:pk>',views.create_gsttax,name='create_gsttax'),

    path('create_lutbond',views.create_lutbond,name='create_lutbond'),

    path('tds/<int:pk>',views.tds,name='tds'),

    path('create_tds/<int:pk>',views.create_tds,name='create_tds'),

    path('person_tds/<int:pk>',views.person_tds,name='person_tds'),

    path('person/<int:pk>',views.person,name='person'),

    path('bank_details',views.bank_details,name='bank_details'),

    path('bankname',views.bankname,name='bankname'),

    path('shut_cmpny',views.shut_cmpny,name='shut_cmpny'),

    path('shut/<int:pk>',views.shut,name='shut'),

    path('enable/<int:pk>',views.enable,name='enable'),

    path('c_rates',views.c_rates,name='c_rates'),

    path('b_name',views.b_name,name='b_name'),

    path('cheque',views.cheque,name='cheque'),

    path('ledger_gst',views.ledger_gst,name='ledger_gst'),

    path('vouch_advance/<int:pk>',views.vouch_advance,name='vouch_advance'),

    path('ledger_chequed',views.ledger_chequed,name='ledger_chequed'),

    path('company',views.company,name='company'),
    path('altercompanyview',views.altercompanyview,name='altercompanyview'),
    path('selectcompany',views.selectcompany,name='selectcompany'),
    path('shutcompany',views.shutcompany,name='shutcompany'),
    path('create_currency/<int:pk>',views.create_currency,name='create_currency'),
    path('altercompany/<int:pk>',views.altercompany,name='altercompany'),
    path('disable/<int:pk>',views.disable,name='disable'),
    path('enable/<int:pk>',views.enable,name='enable'),
    path('alter_currency/<int:pk>',views.alter_currency,name='alter_currency'),

    path('load_centre',views.load_centre,name='load_centre'),

    path('ledger_taxgst',views.ledger_taxgst,name='ledger_taxgst'),

    path('create_voucher/<int:pk>',views.create_voucher,name='create_voucher'),
    path('create_voucher_advance/<int:pk>',views.create_voucher_advance,name='create_voucher_advance'),

    path('create_ROE/<int:pk>',views.create_ROE,name='create_ROE'),

    path('create_ledger<int:pk>',views.create_ledger,name='create_ledger'),

    path('create_ledgerdimension<int:pk>',views.create_ledgerdimension,name='create_ledgerdimension'),

    path('company_create',views.company_create,name='company_create'),

    path('company_feature/<int:cf>',views.company_feature,name='company_feature'),

    path('create_bankdetails',views.create_bankdetails,name='create_bankdetails'),

    path('create_chequebk',views.create_chequebk,name='create_chequebk'),

    path('create_ledger_gst',views.create_ledger_gst,name='create_ledger_gst'),

    # path('create_voucher_advance',views.create_voucher_advance,name='create_voucher_advance'),

    path('create_ledger_taxgst',views.create_ledger_taxgst,name='create_ledger_taxgst'),

    
]