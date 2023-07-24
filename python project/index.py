from tkinter import *  
from tkinter import ttk
from tkinter import messagebox
import random,os
import tempfile

class Bill_app:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x710+0+0")
        self.root.title("Billing software")

       #********Varibles******
        self.C_name=StringVar()#customer
        self.C_mailid=StringVar()#customer
        self.C_mobno=IntVar() #customer
        self.product=StringVar()#product
        self.prices=IntVar()#product
        self.qty=IntVar()
        self.prices1=IntVar()#*grocery
        self.qty1=IntVar()
        self.product1=StringVar()
        self.prices2=IntVar()#*others**
        self.qty2=IntVar()
        self.product2=StringVar()
        self.billno=StringVar()
        z=random.randint(1000,9999)
        self.billno.set(z)
        self.total=StringVar()
        self.SubTotal=StringVar()
        self.SubTotal1=StringVar()
        self.SubTotal2=StringVar()
        self.TAXS=StringVar()
        self.GroTAXS=StringVar()
        self.OtherTAXS=StringVar()
        self.search_bill=StringVar()
        self.product_categ=StringVar()
        self.product_subcateg=StringVar()
        self.product_categI=StringVar()
        self.product_categII=StringVar()
        
        #product categories
        self.category=["select option","Clothing","Lifestyle"]
        #subcategories
        self.subcategcloth=["Select option","Pants","Shirts","T-Shirts","Sarees","Kurtas","Legins","Gowns"]
        self.pants=["Select option","Levies","Mufti","spyker"]
        self.price_levies=5000
        self.price_mufti=1000
        self.price_spyker=1200

        self.Tshirts=["Select option","Polo","Roadster","Jack&Jones"]
        self.price_polo=599      
        self.price_Roadster=399
        self.price_Jack=870

        self.shirts=["Select option","Louis","Peter England","Park Avenue"]
        self.price_louis=599
        self.price_PE=499
        self.price_park=670

        self.sarees=["Select option","satya Paul","Gaurang","Kalanjali"]
        self.price_satya=700
        self.price_Gaurang=570
        self.price_Kalan=999
        
        self.kurtas=["Select option","Rayon","Allensolly","Amukti"]
        self.price_Rayon=599
        self.price_Allen=770
        self.price_Amukti=999
        self.Legins=["Select option","Ajio","LyraLux","BlissClub"]
        self.price_Ajio=599
        self.price_LyrL=499
        self.price_Blis=670
        self.Gowns=["Select option","BerryLush","Global","Soch"]
        self.price_Berrylush=999
        self.price_Global=1500
        self.price_Soch=1200
        #Lifestyle
        self.subcategLifestyle=["Select option","Soaps","Hairoil","Facewash","FaceCream","Shampoo"]

        self.soaps=["Select option","Santoor","Lux","Dove","Medimix","Chandrika"]
        self.price_santoor=40
        self.price_Lux=50
        self.price_Dove=50
        self.price_Medi=40
        self.price_Chand=40

        self.hairoil=["Select option","Parachute","Indhuleka","Eldia"]
        self.price_para=70
        self.price_Indhu=90
        self.price_Eldia=90
        self.facewash=["Select option","Himalaya","Hamam","Ahaglow"]
        self.price_himalaya=90
        self.price_hamam=60
        self.price_Ahaglow=360
        self.facecream=["Select option","Ponds","Fair&lovely","Mamaearth","Lakme"]
        self.price_ponds=120
        self.price_fair=60
        self.price_mamaearth=80
        self.price_lakme=99

        self.shampoo=["Select option","Clinic plus","Chick","Himalaya","Clear","meera"]
        self.price_clinicplus=55
        self.price_chick=55
        self.price_himalya1=70
        self.price_Clear=90
        self.price_meera=60
     
        #Groceries
        self.categ1=["Select option","Rice","Flour","Oil","Millets","Common Items","MasalaPowder","Milk Products"]
        self.subcategRice=["Select option","Mallige","Kohinoor","IndiaGate"]
        self.price_mallige=1200
        self.price_kohinoor=1800
        self.price_Indiagate=1500
        
        self.subcategflour=["Select option","wheat Flour","Ragi Flour","Corn Flour","Rice Flour","Maida"]
        self.price_wheatflour=60
        self.price_ragiflour=60
        self.price_cornflour=65
        self.price_riceflour=50
        self.price_maida=65
       
        self.subcategoil=["Select option","Sunpure","Goldwinner","Palm Oil","Fortune","Olive Oil","Groundnut Oil"]
        self.price_sunpure=130
        self.price_goldwinner=150
        self.price_palm=130
        self.price_fortune=160
        self.price_oliveoil=190
        self.price_groundnut=170
        
        self.subcategmilletes=["Select option","Ragi","Foxtails","Pearl","Broken Wheat","Jowar","Wheat"]
        self.price_Ragi=70
        self.price_foxtail=120
        self.price_pearl=90
        self.price_brokenwheat=60
        self.price_jowar=60
        self.price_wheat=60
        
        self.subcategcommonItems=["Select option","Dals","Mustard","Fenugreek","Rava","Barley","Nuts","Sugar","Chana","Pepper","Jeera","Clove","Poppy"]
        self.price_dals=90
        self.price_mus=40
        self.price_fenu=40
        self.price_rava=45
        self.price_barley=50
        self.price_nuts=80
        self.price_sugar=50
        self.price_chana=45
        self.price_Pepper=20
        self.price_Jeera=20
        self.price_Clove=10
        self.price_Poppy=10

        self.subcategmasala_powder=["Select option","Sambar Powder","Chilli Powder","Coriender Powder","Turmeric Powder"]
        self.price_sambarpowder=50
        self.price_chilli=30
        self.price_coriender=30
        self.price_Turmeric=20
          
        self.subcategmilkproduct=["Milk powder","Ghee","Butter","Paneer"]
        self.price_milk=30
        self.price_ghee=150
        self.price_butter=80
        self.price_paneer=100
    #OtherProducts
        self.categ2=["Select option","Medical products","Bags","Stationary","Others"]
        self.subcategmedi_products=["Select option","boroline","cotton","Bandage","Detol","volinispray"]
        self.price_boroline=80
        self.price_cotton=30
        self.price_bandage=30
        self.price_detol=50
        self.price_volini=70
       
        self.subcategbags=["Select option","School bags","Luggage Bags","Handbags"]
        self.price_schoolbags=500
        self.price_lugg=999
        self.price_handbags=599

        self.subacategstationary=["Select option","Books","A4 sheets","Pens","Sketches","Pencils"]
        self.price_books=50
        self.price_A4=100
        self.price_pens=20
        self.price_sketches=50
        self.price_pencil=35
        self.subcategothers=["Select option","Cool Drinks","Chocolates","Snacks"]
        self.price_col=45
        self.price_choco=20
        self.price_snacks=20
        
    
      #cust details
        F1=LabelFrame(self.root,bg="#0a4d68",relief=GROOVE,bd=8)
        F1.place(x=2,y=0,width=1350,height=690)

        Title=LabelFrame(F1,bg="#0a4d68",relief=GROOVE,bd=8)
        Title.place(x=10,y=2,width=1320,height=60)
        title=Label(Title,text="BILLING SOFTWARE",font=("times new roman",24,"bold"),bg="#0a4d68",fg="#ecf8f9",relief=GROOVE)
        title.place(x=480,y=3)


        customer=LabelFrame(F1,bg="#ecf8f9",relief=GROOVE,bd=6)
        customer.place(x=10,y=140,width=460,height=150)

        self.cust=Label(customer,text="Customer Details",font=("times new roman",14,"bold"),bg="#0a4d68",fg="#ecf8f9",relief=GROOVE)
        self.cust.grid(row=0,column=0,sticky=W,padx=5,pady=3)
        

        self.Name=Label(customer,text="NAME",font=("times new roman",14,"bold"),bg="#ecf8f9",fg="#0a4d68")
        self.Name.grid(row=1,column=0,sticky=W,padx=5,pady=3)
        self.txtName=ttk.Entry(customer,textvariable=self.C_name,font=("times new roman",12,"bold"),width=30)
        self.txtName.grid(row=1,column=2,padx=5,pady=3)

        self.mailid=Label(customer,text="Mail id",font=("times new roman",14,"bold"),fg="#0a4d68",bg="#ecf8f9")
        self.mailid.grid(row=2,column=0,sticky=W,padx=5,pady=3)
        self.txtmailid=ttk.Entry(customer,textvariable=self.C_mailid,font=("times new roman",12,"bold"),width=30)
        self.txtmailid.grid(row=2,column=2,padx=5,pady=3)

        self.label_mob=Label(customer,text="Mobile No",font=("times new roman",14,"bold"),fg="#0a4d68",bg="#ecf8f9")
        self.label_mob.grid(row=3,column=0,sticky=W,padx=5,pady=3)
        self.entry_mob=ttk.Entry(customer,textvariable=self.C_mobno,font=("times new roman",12,"bold"),width=30)
        self.entry_mob.grid(row=3,column=2,padx=5,pady=3)
      
      #product details
        prod_name=LabelFrame(F1,bg="#ecf8f9",relief=GROOVE,bd=6)
        prod_name.place(x=10,y=300,width=460,height=230)

        self.ProdDet=Label(prod_name,text="Products",font=("times new roman",14,"bold"),bg="#0a4d68",fg="#ecf8f9",relief=GROOVE)
        self.ProdDet.grid(row=0,column=0,sticky=W,padx=5,pady=3)
         #categ
        self.categ=Label(prod_name,text="Select Categories",font=("times new roman",14,"bold"),fg="#0a4d68",bg="#ecf8f9")
        self.categ.grid(row=1,column=0,sticky=W,padx=5,pady=3)

        self.combocateg=ttk.Combobox(prod_name,textvariable=self.product_categ,value=self.category,font=("times new roman",12,"bold"),width=20)
        self.combocateg.current(0)
        self.combocateg.grid(row=1,column=2,padx=3,pady=3)
        self.combocateg.bind("<<ComboboxSelected>>",self.categories)

        #sub Categ
        self.subcateg=Label(prod_name,text="Subcategory",font=("times new roman",14,"bold"),fg="#0a4d68",bg="#ecf8f9")
        self.subcateg.grid(row=2,column=0,sticky=W,padx=5,pady=3)

        self.combosubcateg=ttk.Combobox(prod_name,textvariable=self.product_subcateg,value=[" "],font=("times new roman",12,"bold"),width=20)
        self.combosubcateg.grid(row=2,column=2,padx=3,pady=3)
        self.combosubcateg.bind("<<ComboboxSelected>>",self.productadd,self.prod_price)
        
        
        self.productName=Label(prod_name,text="Product name",font=("times new roman",14,"bold"),fg="#0a4d68",bg="#ecf8f9")
        self.productName.grid(row=3,column=0,sticky=W,padx=5,pady=3)

        self.comboproductName=ttk.Combobox(prod_name,textvariable=self.product,font=("times new roman",12,"bold"),width=20)
        self.comboproductName.grid(row=3,column=2,padx=3,pady=3)
        self.comboproductName.bind("<<ComboboxSelected>>",self.prod_price)

        self.pri=Label(prod_name,text="Price",font=("times new roman",14,"bold"),fg="#0a4d68",bg="#ecf8f9")
        self.pri.grid(row=4,column=0,sticky=W,padx=5,pady=3)

        self.combopri=ttk.Combobox(prod_name,textvariable=self.prices,font=("times new roman",12,"bold"),width=20)
        self.combopri.grid(row=4,column=2,padx=3,pady=3)

        self.quantity=Label(prod_name,text="Quantitiy",font=("times new roman",14,"bold"),fg="#0a4d68",bg="#ecf8f9")
        self.quantity.grid(row=5,column=0,sticky=W,padx=5,pady=5)

        self.txtquantity=ttk.Entry(prod_name,textvariable=self.qty,font=("times new roman",14,"bold"),width=18)
        self.txtquantity.grid(row=5,column=2,padx=3,pady=3)
        
        self.add=Button(prod_name,command=self.additems,width=6,height=1, text="ADD",font=("arial",14,"bold"),bd=4,bg="#0a4d68",fg="#ecf8f9",relief=GROOVE)
        self.add.place(x=350,y=180 )
       
        #groceries
        grocery=LabelFrame(F1,relief=GROOVE,bd=6,bg="#ecf8f9")
        grocery.place(x=920,y=140,width=400,height=220)
        self.gro=Label(grocery,text="Groceries",font=("times new roman",14,"bold"),bg="#0a4d68",fg="#ecf8f9",relief=GROOVE)
        self.gro.grid(row=0,column=0,sticky=W,padx=3,pady=3)
       #categ
        self.categI=Label(grocery,text="Select Categories",font=("times new roman",14,"bold"),fg="#0a4d68",bg="#ecf8f9")
        self.categI.grid(row=1,column=0,sticky=W,padx=3,pady=2)
        self.combocategI=ttk.Combobox(grocery,textvariable=self.product_categI,value=self.categ1,font=("times new roman",12,"bold"),width=20)
        self.combocategI.current(0)
        self.combocategI.grid(row=1,column=2,padx=3,pady=2)
        self.combocategI.bind("<<ComboboxSelected>>",self.categories1)
        #sub Categ
        self.subcategI=Label(grocery,text="Subcategory",font=("times new roman",14,"bold"),fg="#0a4d68",bg="#ecf8f9")
        self.subcategI.grid(row=2,column=0,sticky=W,padx=3,pady=3)
        self.combosubcategI=ttk.Combobox(grocery,textvariable=self.product1,font=("times new roman",12,"bold"),width=20)
        self.combosubcategI.grid(row=2,column=2,padx=3,pady=3)
        self.combosubcategI.bind("<<ComboboxSelected>>",self.prod_price1)

        self.priceI=Label(grocery,text="Price",font=("times new roman",14,"bold"),fg="#0a4d68",bg="#ecf8f9")
        self.priceI.grid(row=3,column=0,sticky=W,padx=3,pady=3)
        self.combopriceI=ttk.Combobox(grocery,textvariable=self.prices1,font=("times new roman",12,"bold"),width=20)
        self.combopriceI.grid(row=3,column=2,padx=3,pady=3)

        self.quantityI=Label(grocery,text="Quantitiy",font=("times new roman",14,"bold"),fg="#0a4d68",bg="#ecf8f9")
        self.quantityI.grid(row=4,column=0,sticky=W,padx=3,pady=3)
        self.txtquantityI=ttk.Entry(grocery,textvariable=self.qty1,font=("times new roman",12,"bold"),width=22)
        self.txtquantityI.grid(row=4,column=2,padx=3,pady=3)
        
        self.addI=Button(grocery,command=self.additemsg, width=6,height=1, text="ADD",font=("arial",14,"bold"),border=4,fg="#ecf8f9",bg="#0a4d68",relief=GROOVE)
        self.addI.place(x=290,y=170)
       # other products   
        OP=LabelFrame(F1,relief=GROOVE,bd=6,bg="#ecf8f9")
        OP.place(x=920,y=370,width=400,height=220)
        self.OtherP=Label(OP,text="Others",font=("times new roman",14,"bold"),bg="#0a4d68",fg="#ecf8f9",relief=GROOVE)
        self.OtherP.grid(row=0,column=0,sticky=W,padx=3,pady=3)

       #categ
        self.categII=Label(OP,text="Select Categories",font=("times new roman",14,"bold"),fg="#0a4d68",bg="#ecf8f9")
        self.categII.grid(row=1,column=0,sticky=W,padx=3,pady=3)

        self.combocategII=ttk.Combobox(OP,value=self.categ2,font=("times new roman",12,"bold"),width=20)
        self.combocategII.current(0)
        self.combocategII.grid(row=1,column=2,padx=3,pady=3)
        self.combocategII.bind("<<ComboboxSelected>>",self.categories2)

        #sub Categ
        self.subcategII=Label(OP,text="Subcategory",font=("times new roman",14,"bold"),fg="#0a4d68",bg="#ecf8f9")
        self.subcategII.grid(row=2,column=0,sticky=W,padx=3,pady=3)
        self.combosubcategII=ttk.Combobox(OP,textvariable=self.product2,font=("times new roman",12,"bold"),width=20)
        self.combosubcategII.grid(row=2,column=2,padx=3,pady=3)
        self.combosubcategII.bind("<<ComboboxSelected>>",self.prod_price2)
      

        self.priceII=Label(OP,text="Price",font=("times new roman",14,"bold"),fg="#0a4d68",bg="#ecf8f9")
        self.priceII.grid(row=3,column=0,sticky=W,padx=3,pady=3)
        self.combopriceII=ttk.Combobox(OP,textvariable=self.prices2,font=("times new roman",12,"bold"),width=20)
        self.combopriceII.grid(row=3,column=2,padx=3,pady=3)

        self.quantityII=Label(OP,text="Quantitiy",font=("times new roman",14,"bold"),fg="#0a4d68",bg="#ecf8f9")
        self.quantityII.grid(row=4,column=0,sticky=W,padx=3,pady=3)
        self.txtquantityII=ttk.Entry(OP,textvariable=self.qty2,font=("times new roman",12,"bold"),width=22)
        self.txtquantityII.grid(row=4,column=2,padx=3,pady=3)

        self.addII=Button(OP,command=self.additemsO, width=6,height=1, text="ADD",font=("arial",14,"bold"),fg="#ecf8f9",bg="#0a4d68",relief=GROOVE,bd=4)
        self.addII.place(x=290,y=170)
         
  
        #bill counter
        cal1=LabelFrame(F1,relief=GROOVE,bd=6,bg="#0a4d68")
        cal1.place(x=10,y=540,width=690,height=130)
        
        
        self.protax=Label(cal1,text="Product Tax",font=("times new roman",12,"bold"),fg="#0a4d68",bg="#ecf8f9")
        self.protax.grid(row=0,column=0,sticky=W,padx=3,pady=5)
        self.txtprotax=ttk.Entry(cal1,textvariable=self.TAXS,font=("times new roman",12,"bold"),width=12)
        self.txtprotax.grid(row=0,column=1,padx=3,pady=5)
        
        self.groTax=Label(cal1,text="Grocery Tax",font=("times new roman",12,"bold"),fg="#0a4d68",bg="#ecf8f9")
        self.groTax.grid(row=1,column=0,sticky=W,padx=3,pady=5)
        self.txtgroTax=ttk.Entry(cal1,textvariable=self.GroTAXS,font=("times new roman",12,"bold"),width=12)
        self.txtgroTax.grid(row=1,column=1,padx=3,pady=5)

        self.tx=Label(cal1,text="Others Tax",font=("times new roman",12,"bold"),fg="#0a4d68",bg="#ecf8f9")
        self.tx.grid(row=2,column=0,sticky=W,padx=3,pady=5)
        self.txttx=ttk.Entry(cal1,textvariable=self.OtherTAXS,font=("times new roman",12,"bold"),width=12)
        self.txttx.grid(row=2,column=1,padx=3,pady=5)

        self.Total=Label(cal1,text="Total product price",font=("times new roman",12,"bold"),fg="#0a4d68",bg="#ecf8f9")
        self.Total.grid(row=0,column=2,sticky=W,padx=8,pady=5)
        self.txtTotal=ttk.Entry(cal1,textvariable=self.SubTotal,font=("times new roman",12,"bold"),width=12)
        self.txtTotal.grid(row=0,column=3,padx=3,pady=5)
        
        self.Total1=Label(cal1,text="Total grocery price",font=("times new roman",12,"bold"),fg="#0a4d68",bg="#ecf8f9")
        self.Total1.grid(row=1,column=2,sticky=W,padx=8,pady=5)
        self.txtTotal1=ttk.Entry(cal1,textvariable=self.SubTotal1,font=("times new roman",12,"bold"),width=12)
        self.txtTotal1.grid(row=1,column=3,padx=3,pady=5)

        self.Total2=Label(cal1,text="Others total price",font=("times new roman",12,"bold"),fg="#0a4d68",bg="#ecf8f9")
        self.Total2.grid(row=2,column=2,sticky=W,padx=8,pady=5)
        self.txtTotal2=ttk.Entry(cal1,textvariable=self.SubTotal2,font=("times new roman",12,"bold"),width=12)
        self.txtTotal2.grid(row=2,column=3,padx=3,pady=5)

        self.Total3=Label(cal1,text="Total ",font=("times new roman",14,"bold"),fg="#0a4d68",bg="#ecf8f9")
        self.Total3.grid(row=1,column=4,sticky=W,padx=8,pady=5)
        self.txtTotal3=ttk.Entry(cal1,textvariable=self.total,font=("times new roman",16,"bold"),width=12)
        self.txtTotal3.grid(row=1,column=5,padx=3,pady=5)
       
         #bill system 
        bill=LabelFrame(F1,bg="white",relief=GROOVE,bd=8)
        bill.place(x=500,y=140,width=400,height=370)

        scroll_y=Scrollbar(bill,orient=VERTICAL)
        self.textarea=Text(bill,yscrollcommand=scroll_y.set,bg="white",fg="black",font=("times new roman",12,"bold"))
        scroll_y.pack(side=RIGHT,fil=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)
        self.message()
        #topframe
        F2=LabelFrame(F1,bg="#ecf8f9",relief=GROOVE,bd=6)
        F2.place(x=10,y=70,width=1310,height=50)

        self.bill_no=Label(F2,text="Bill number",font=("times new roman",14,"bold"),bg="#ecf8f9",fg="#3c486b")
        self.bill_no.grid(row=0,column=0,sticky=W,padx=10,pady=5)
        self.txtbill_no=ttk.Entry(F2,textvariable=self.search_bill,font=("times new roman",14,"bold"),width=12)
        self.txtbill_no.grid(row=0,column=2,padx=10,pady=5)

        self.search=Button(F2,width=8,command=self.find_bill,height=1,text="search",font=("arial",12,"bold"),bg="#0a4d68",fg="white")
        self.search.grid(row=0,column=3,padx=5,pady=5)

        self.Print=Button(F2,command=self.print_bill,width=8,height=1,text="Print",font=("arial",12,"bold"),bg="#0a4d68",fg="white")
        self.Print.place(x=1100,y=5)

        self.Exit=Button(F2,command=self.root.destroy,width=8,height=1,text="Exit",font=("arial",12,"bold"),bg="#0a4d68",fg="white")
        self.Exit.place(x=1200,y=5)


      #bottom frame
        bottom=LabelFrame(F1,bg="#ecf8f9",relief=GROOVE,bd=8)
        bottom.place(x=720,y=600,width=600,height=70)
        
        self.Tot=Button(bottom,command=self.bill_taxs,width=10,height=1, text="Total",font=("arial",14,"bold"),bg="#0a4d68",fg="white")
        self.Tot.grid(row=1,column=1,padx=10,pady=5)
        
        self.generate=Button(bottom,command=self.gen_bill,width=10,height=1,text="Generate Bill",font=("arial",14,"bold"),bg="#0a4d68",fg="white")
        self.generate.grid(row=1,column=2,padx=5,pady=5)

        self.save=Button(bottom,command=self.save_bill,width=10,height=1,text="save",font=("arial",14,"bold"),bg="#0a4d68",fg="white")
        self.save.grid(row=1,column=3,padx=5,pady=3)
        
        self.Reset=Button(bottom,command=self.clear_bill,width=10,height=1,text="Reset",font=("arial",14,"bold"),bg="#0a4d68",fg="white")
        self.Reset.grid(row=1,column=4,padx=5,pady=3)
   
        self.L=[] 
        self.L1=[]
        self.L2=[]
        
        
    def additems(self):
         self.a=self.prices.get()
         self.b=self.qty.get()*self.a
         self.L.append(self.b)
         self.textarea.insert(END,f"\n{self.product.get()}\t\t\t{self.qty.get()}\t{self.b}")      
    def additemsg(self):
            self.c=self.prices1.get()
            self.d=self.qty1.get()*self.c  
            self.L1.append(self.d)              
            self.textarea.insert(END,f"\n{self.product1.get()}\t\t\t{self.qty1.get()}\t{self.d}")          
    def additemsO(self):  
            self.E=self.prices2.get()
            self.f=self.qty2.get()*self.E
            self.L2.append(self.f)
            self.textarea.insert(END,f"\n{self.product2.get()}\t\t\t{self.qty2.get()}\t{self.f}")


       #********BILL AREA*******
    def message(self):
      self.textarea.delete(1.0,END)
      self.textarea.insert(END,"\t Welcome to our Shop")
      self.textarea.insert(END,f"\n Bill Number:{self.billno.get()}")
      self.textarea.insert(END,f"\n Customer Name:{self.C_name.get()}") 
      self.textarea.insert(END,f"\n Phone Number:{self.C_mobno.get()}")
      self.textarea.insert(END,f"\n Customer Email:{self.C_mailid.get()}") 
   
      self.textarea.insert(END,"\n -----------------------------------------------------------------------         ")
      self.textarea.insert(END,f"\n Products\t\t\tQTY\tPrice")
      self.textarea.insert(END,"\n  -----------------------------------------------------------------------        \n ")

    def bill_taxs(self):
         Tax=1
         
         if self.prices!="":
            self.A=(((sum(self.L))-(self.prices.get()))*Tax)
            self.TAXS.set(str('Rs.%.2f'%((self.A)/100)))
            self.PT=round(((sum(self.L))+(self.A)/100))
            self.T=self.SubTotal.set(str('Rs.%.2f'%(self.PT)))
          
         if self.prices1!="":
            self.B=(((sum(self.L1))-(self.prices1.get()))*Tax)
            self.GroTAXS.set(str('Rs.%.2f'%((self.B)/100)))
            self.G=round((sum(self.L1))+((self.B)/100))
            self.SubTotal1.set(str('Rs.%.2f'%(self.G)))

         if self.prices2!="":
            self.C=(((sum(self.L2))-(self.prices2.get()))*Tax)
            self.OtherTAXS.set(str('Rs.%.2f'%((self.C)/100)))
            self.D=round((sum(self.L2))+((self.C)/100))
            self.SubTotal2.set(str('Rs.%.2f'%(self.D)))
         
         self.t=((self.PT)+
                        (self.G)+
                        (self.D))
         self.total.set(str('Rs.%.2f'%(self.t))) 
    def save_bill(self):
       sb=messagebox.askyesno("Save Bill","Do you want to save")
       if sb>0:
          self.bill_data=self.textarea.get(1.0,END)
          f1=open('bills/'+str(self.billno.get())+".txt",'w')
          f1.write(self.bill_data)
          sb=messagebox.showinfo("Saved",f"Bill No:{self.billno.get()} Saved successfully")
          f1.close()
    def clear_bill(self): 
        self.textarea.delete(1.0,END)
        self.C_name.set("")
        self.C_mailid.set("")
        self.C_mobno.set(0)
        self.product.set("")
        self.prices.set(0)
        self.qty.set(0)
        self.prices1.set(0)
        self.qty1.set(0)
        self.product1.set("")
        self.prices2.set(0)
        self.qty2.set(0)
        self.product2.set("")
        z=random.randint(1000,9999)
        self.billno.set(z)
        self.billno.set(str(z))
        self.total.set("")
        self.SubTotal.set("")
        self.SubTotal1.set("")
        self.SubTotal2.set("")
        self.TAXS.set("")
        self.GroTAXS.set("")
        self.OtherTAXS.set("")
        self.search_bill.set("")
        self.product_categ.set("Select option") 
        self.product_subcateg.set("")
        self.product_categI.set("Select option")
        self.product_categII.set("Select option")
        self.L=[0]
        self.L1=[0]
        self.L2=[0]
        self.message()

    def print_bill(self):
       q=self.textarea.get(1.0,"end-1c")
       filename=tempfile.mktemp('.txt')
       open(filename,'w').write(q)
       os.startfile(filename,"print")

    def find_bill(self):
       found="no"
       for i in os.listdir("bills"):
          if i.split('.')[0]==self.search_bill.get():
             f1=open(f'bills/{i}','r')
             self.textarea.delete(1.0,END)
             for d in f1:
                self.textarea.insert(END,d)
             f1.close()
             found="yes"
       if found=="no":
          messagebox.showerror("Error","Invalid Bill no.")
    
     
    def gen_bill(self): 
          if self.TAXS.get()!="":
           text=self.textarea.get(9.0,(9.0+float(len(self.L))+
                                           float(len(self.L1))+
                                           float(len(self.L2))))
           self.message()
           self.textarea.insert(END,text)
           self.textarea.insert(END,"\n--------------------------------------------------------------------")
           self.textarea.insert(END,f"\n Product Tax:\t\t\t{self.TAXS.get()}")
           self.textarea.insert(END,f"\n Total product price:\t\t{self.SubTotal.get()}")
           self.textarea.insert(END,"\n--------------------------------------------------------------------")
          if self.GroTAXS.get()!="":
           self.textarea.insert(END,"\n--------------------------------------------------------------------")
           self.textarea.insert(END,f"\n Grocery Tax:\t\t\t{self.GroTAXS.get()}")
           self.textarea.insert(END,f"\n Total Grocery price:\t\t{self.SubTotal1.get()}")
           self.textarea.insert(END,"\n--------------------------------------------------------------------")
          if self.OtherTAXS.get()!="":
           self.textarea.insert(END,"\n--------------------------------------------------------------------")
           self.textarea.insert(END,f"\n Other product Tax:\t\t\t{self.OtherTAXS.get()}")
           self.textarea.insert(END,f"\n Total other  price:\t\t{self.SubTotal2.get()}")
           self.textarea.insert(END,"\n--------------------------------------------------------------------")
          if self.total.get()!="":
           self.textarea.insert(END,"\n--------------------------------------------------------------------")
           self.textarea.insert(END,f"\n Total Amount :\t\t\t{self.total.get()}")
           self.textarea.insert(END,"\n--------------------------------------------------------------------")
             
    def categories(self,event=""):
        if self.combocateg.get()=="Clothing":
            self.combosubcateg.config(value=self.subcategcloth)
            self.combosubcateg.current(0)
        if self.combosubcateg.get()=="Select option":
           self.comboproductName.set(0)
           self.combopri.set(0)
      
        if self.combocateg.get()=="Lifestyle":
            self.combosubcateg.config(value=self.subcategLifestyle)
            self.combosubcateg.current(0)
        if self.combosubcateg.get()=="Select option":
           self.comboproductName.set(0)
           self.combopri.set(0) 
    
    def productadd(self,event=""):
        if self.combosubcateg.get()=="Pants":
            self.comboproductName.config(value=self.pants)
            self.comboproductName.current(0)
        if self.comboproductName.get()=="Select option":
            self.combopri.set(0) 
      #shirts
        if self.combosubcateg.get()=="Shirts":
            self.comboproductName.config(value=self.shirts)
            self.comboproductName.current(0)
        if self.comboproductName.get()=="Select option":
            self.combopri.set(0) 

       #T-shirts        
        if self.combosubcateg.get()=="T-Shirts":
            self.comboproductName.config(value=self.Tshirts)
            self.comboproductName.current(0)
        if self.comboproductName.get()=="Select option":
            self.combopri.set(0)  
        
        if self.combosubcateg.get()=="Sarees":
            self.comboproductName.config(value=self.sarees)
            self.comboproductName.current(0)
        if self.comboproductName.get()=="Select option":
            self.combopri.set(0) 
        
        if self.combosubcateg.get()=="Kurtas":
            self.comboproductName.config(value=self.kurtas)
            self.comboproductName.current(0)
        if self.comboproductName.get()=="Select option":
            self.combopri.set(0) 
        
        if self.combosubcateg.get()=="Legins":
            self.comboproductName.config(value=self.Legins)
            self.comboproductName.current(0)
        if self.comboproductName.get()=="Select option":
            self.combopri.set(0) 
        
        if self.combosubcateg.get()=="Gowns":
            self.comboproductName.config(value=self.Gowns)
            self.comboproductName.current(0)
        if self.comboproductName.get()=="Select option":
            self.combopri.set(0) 
       
        if self.combosubcateg.get()=="Soaps":
            self.comboproductName.config(value=self.soaps)
            self.comboproductName.current(0)
        if self.comboproductName.get()=="Select option":
            self.combopri.set(0) 
        
        if self.combosubcateg.get()=="Hairoil":
            self.comboproductName.config(value=self.hairoil)
            self.comboproductName.current(0)
        if self.comboproductName.get()=="Select option":
            self.combopri.set(0)  
       
        if self.combosubcateg.get()=="Facewash":
            self.comboproductName.config(value=self.facewash)
            self.comboproductName.current(0)
        if self.comboproductName.get()=="Select option":
            self.combopri.set(0) 
        
        if self.combosubcateg.get()=="FaceCream":
            self.comboproductName.config(value=self.facecream)
            self.comboproductName.current(0)
        if self.comboproductName.get()=="Select option":
            self.combopri.set(0) 
        
        if self.combosubcateg.get()=="Shampoo":
            self.comboproductName.config(value=self.shampoo)
            self.comboproductName.current(0)  
        if self.comboproductName.get()=="Select option":
            self.combopri.set(0)        

    def prod_price(self,event=""):
        if self.comboproductName.get()=="Levies":
            self.combopri.config(value=self.price_levies)
            self.combopri.current(0)
            self.qty.set(1)    
        
        if self.comboproductName.get()=="Mufti":
            self.combopri.config(value=self.price_mufti)
            self.combopri.current(0)
            self.qty.set(1)

        if self.comboproductName.get()=="spyker":
           self.combopri.config(value=self.price_spyker)
           self.combopri.current(0)
           self.qty.set(1)

         #Tshirts
        if self.comboproductName.get()=="Polo":
           self.combopri.config(value=self.price_polo)
           self.combopri.current(0)
           self.qty.set(1)
        if self.comboproductName.get()=="Roadster":
          self.combopri.config(value=self.price_Roadster)
          self.combopri.current(0)
          self.qty.set(1)

        if self.comboproductName.get()=="Jack&Jones":
           self.combopri.config(value=self.price_Jack)
           self.combopri.current(0)
           self.qty.set(1)
         
          #shirts
        if self.comboproductName.get()=="Louis":
            self.combopri.config(value=self.price_louis)
            self.combopri.current(0)
            self.qty.set(1)
        if self.comboproductName.get()=="Peter England":
          self.combopri.config(value=self.price_PE)
          self.combopri.current(0)
          self.qty.set(1)

        if self.comboproductName.get()=="Park Avenue":
          self.combopri.config(value=self.price_park)
          self.combopri.current(0)
          self.qty.set(1)
       
          #sarees
        if self.comboproductName.get()=="satya Paul":
           self.combopri.config(value=self.price_satya)
           self.combopri.current(0)
           self.qty.set(1)    
        if self.comboproductName.get()=="Gaurang":
          self.combopri.config(value=self.price_Gaurang)
          self.combopri.current(0)
          self.qty.set(1)

        if self.comboproductName.get()=="Kalanjali":
          self.combopri.config(value=self.price_Kalan)
          self.combopri.current(0)
          self.qty.set(1)
          #kurtas
        if self.comboproductName.get()=="Rayon":
         self.combopri.config(value=self.price_Rayon)
         self.combopri.current(0)
         self.qty.set(1)

        if self.comboproductName.get()=="Allensolly":
          self.combopri.config(value=self.price_Allen)
          self.combopri.current(0)
          self.qty.set(1)

        if self.comboproductName.get()=="Amukti":
          self.combopri.config(value=self.price_Amukti)
          self.combopri.current(0)
          self.qty.set(1)
           #legins
        if self.comboproductName.get()=="Ajio":
            self.combopri.config(value=self.price_Ajio)
            self.combopri.current(0)
            self.qty.set(1)

        if self.comboproductName.get()=="LyraLux":
          self.combopri.config(value=self.price_LyrL)
          self.combopri.current(0)
          self.qty.set(1)

        if self.comboproductName.get()=="BlissClub":
          self.combopri.config(value=self.price_Blis)
          self.combopri.current(0)
          self.qty.set(1)
          #gowns
        if self.comboproductName.get()=="BerryLush":
          self.combopri.config(value=self.price_Berrylush)
          self.combopri.current(0)
          self.qty.set(1)

        if self.comboproductName.get()=="Global":
          self.combopri.config(value=self.price_Global)
          self.combopri.current(0)
          self.qty.set(1)

        if self.comboproductName.get()=="Soch":
          self.combopri.config(value=self.price_Soch)
          self.combopri.current(0)
          self.qty.set(1)
           #lifestyle
        if self.comboproductName.get()=="Santoor":
         self.combopri.config(value=self.price_santoor)
         self.combopri.current(0)
         self.qty.set(1)

        if self.comboproductName.get()=="Lux":
          self.combopri.config(value=self.price_Lux)
          self.combopri.current(0)
          self.qty.set(1)

        if self.comboproductName.get()=="Dove":
          self.combopri.config(value=self.price_Dove)
          self.combopri.current(0)
          self.qty.set(1)
        
        if self.comboproductName.get()=="Medimix":
          self.combopri.config(value=self.price_Medi)
          self.combopri.current(0)
          self.qty.set(1)
        
        if self.comboproductName.get()=="Chandrika":
          self.combopri.config(value=self.price_Chand)
          self.combopri.current(0)
          self.qty.set(1)
          #hairoil
        if self.comboproductName.get()=="Parachute":
          self.combopri.config(value=self.price_para)
          self.combopri.current(0)
          self.qty.set(1)
          
        if self.comboproductName.get()=="Indhuleka":
          self.combopri.config(value=self.price_Indhu)
          self.combopri.current(0)
          self.qty.set(1)  

        if self.comboproductName.get()=="Eldia":
          self.combopri.config(value=self.price_Eldia)
          self.combopri.current(0)
          self.qty.set(1)   
          #facewash
        if self.comboproductName.get()=="Himalaya":
          self.combopri.config(value=self.price_himalaya)
          self.combopri.current(0)
          self.qty.set(1)

        if self.comboproductName.get()=="Hamam":
          self.combopri.config(value=self.price_hamam)
          self.combopri.current(0)
          self.qty.set(1)

        if self.comboproductName.get()=="Ahaglow":
          self.combopri.config(value=self.price_Ahaglow)
          self.combopri.current(0)
          self.qty.set(1)
        #facecream
        if self.comboproductName.get()=="Ponds":
          self.combopri.config(value=self.price_ponds)
          self.combopri.current(0)
          self.qty.set(1)
        
        if self.comboproductName.get()=="Fair&lovely":
          self.combopri.config(value=self.price_fair)
          self.combopri.current(0)
          self.qty.set(1)

        if self.comboproductName.get()=="Mamaearth":
          self.combopri.config(value=self.price_mamaearth)
          self.combopri.current(0)
          self.qty.set(1)
        
        if self.comboproductName.get()=="Lakme":
          self.combopri.config(value=self.price_lakme)
          self.combopri.current(0)
          self.qty.set(1)

           #shampoo
        if self.comboproductName.get()=="Clinic plus":
          self.combopri.config(value=self.price_clinicplus)
          self.combopri.current(0)
          self.qty.set(1)
        
        if self.comboproductName.get()=="Chick":
          self.combopri.config(value=self.price_chick)
          self.combopri.current(0)
          self.qty.set(1)

        if self.comboproductName.get()=="Himalaya":
          self.combopri.config(value=self.price_himalya1)
          self.combopri.current(0)
          self.qty.set(1)

        if self.comboproductName.get()=="Clear":
          self.combopri.config(value=self.price_Clear)
          self.combopri.current(0)
          self.qty.set(1)
        
        if self.comboproductName.get()=="meera":
          self.combopri.config(value=self.price_meera)
          self.combopri.current(0)
          self.qty.set(1)
    
       #Groceries
    def categories1(self,event=""):
        if self.combocategI.get()=="Rice":
           self.combosubcategI.config(value=self.subcategRice)
           self.combosubcategI.current(0)
        if self.combosubcategI.get()=="Select option":
          self.combopriceI.set(0)

        if self.combocategI.get()=="Flour":
           self.combosubcategI.config(value=self.subcategflour)
           self.combosubcategI.current(0)
        if self.combosubcategI.get()=="Select option":
          self.combopriceI.set(0)
           
        if self.combocategI.get()=="Oil":
           self.combosubcategI.config(value=self.subcategoil)
           self.combosubcategI.current(0)
        if self.combosubcategI.get()=="Select option":
          self.combopriceI.set(0)
           
        if self.combocategI.get()=="Millets":
           self.combosubcategI.config(value=self.subcategmilletes)
           self.combosubcategI.current(0)
        if self.combosubcategI.get()=="Select option":
          self.combopriceI.set(0)   
        
        if self.combocategI.get()=="Common Items":
           self.combosubcategI.config(value=self.subcategcommonItems)
           self.combosubcategI.current(0)
        if self.combosubcategI.get()=="Select option":
          self.combopriceI.set(0)   
        
        if self.combocategI.get()=="MasalaPowder":
           self.combosubcategI.config(value=self.subcategmasala_powder)
           self.combosubcategI.current(0)
        if self.combosubcategI.get()=="Select option":
          self.combopriceI.set(0)

        if self.combocategI.get()=="Milk Products":
           self.combosubcategI.config(value=self.subcategmilkproduct)
           self.combosubcategI.current(0)
        if self.combosubcategI.get()=="Select option":
          self.combopriceI.set(0)
        
    def prod_price1(self,event=""):
       if self.combosubcategI.get()=="Mallige":
          self.combopriceI.config(value=self.price_mallige)
          self.combopriceI.current(0)
          self.qty1.set(1)
        
       if self.combosubcategI.get()=="Kohinoor":
          self.combopriceI.config(value=self.price_kohinoor)
          self.combopriceI.current(0)
          self.qty1.set(1)
        
       if self.combosubcategI.get()=="IndiaGate":
          self.combopriceI.config(value=self.price_Indiagate)
          self.combopriceI.current(0)
          self.qty1.set(1)
        
       if self.combosubcategI.get()=="wheat Flour":
          self.combopriceI.config(value=self.price_wheatflour)
          self.combopriceI.current(0)
          self.qty1.set(1)
        
       if self.combosubcategI.get()=="Ragi Flour":
          self.combopriceI.config(value=self.price_ragiflour)
          self.combopriceI.current(0)
          self.qty1.set(1)
        
       if self.combosubcategI.get()=="Corn Flour":
          self.combopriceI.config(value=self.price_cornflour)
          self.combopriceI.current(0)
          self.qty1.set(1)

       if self.combosubcategI.get()=="Rice Flour":
          self.combopriceI.config(value=self.price_riceflour)
          self.combopriceI.current(0)
          self.qty1.set(1)
        
       if self.combosubcategI.get()=="Maida":
          self.combopriceI.config(value=self.price_maida)
          self.combopriceI.current(0)
          self.qty1.set(1)
         #oil  
       if self.combosubcategI.get()=="Sunpure":
          self.combopriceI.config(value=self.price_sunpure)
          self.combopriceI.current(0)
          self.qty1.set(1)
        
       if self.combosubcategI.get()=="Goldwinner":
          self.combopriceI.config(value=self.price_goldwinner)
          self.combopriceI.current(0)
          self.qty1.set(1)
        
       if self.combosubcategI.get()=="Palm Oil":
          self.combopriceI.config(value=self.price_palm)
          self.combopriceI.current(0)
          self.qty1.set(1)
        
       if self.combosubcategI.get()=="Fortune":
          self.combopriceI.config(value=self.price_fortune)
          self.combopriceI.current(0)
          self.qty1.set(1)
       
       if self.combosubcategI.get()=="Olive Oil":
          self.combopriceI.config(value=self.price_oliveoil)
          self.combopriceI.current(0)
          self.qty1.set(1)
        
       if self.combosubcategI.get()=="Groundnut Oil":
          self.combopriceI.config(value=self.price_groundnut)
          self.combopriceI.current(0)
          self.qty1.set(1)
        #
       if self.combosubcategI.get()=="Ragi":
          self.combopriceI.config(value=self.price_Ragi)
          self.combopriceI.current(0)
          self.qty1.set(1)  

       if self.combosubcategI.get()=="Foxtails":
          self.combopriceI.config(value=self.price_foxtail)
          self.combopriceI.current(0)
          self.qty1.set(1)
        
       if self.combosubcategI.get()=="Pearl":
          self.combopriceI.config(value=self.price_pearl)
          self.combopriceI.current(0)
          self.qty1.set(1)
        
       if self.combosubcategI.get()=="Broken Wheat":
          self.combopriceI.config(value=self.price_brokenwheat)
          self.combopriceI.current(0)
          self.qty1.set(1)  
       if self.combosubcategI.get()=="Jowar":
          self.combopriceI.config(value=self.price_jowar)
          self.combopriceI.current(0)
          self.qty1.set(1)
        
       if self.combosubcategI.get()=="Wheat":
          self.combopriceI.config(value=self.price_wheat)
          self.combopriceI.current(0)
          self.qty1.set(1)
        #
       if self.combosubcategI.get()=="Dals":
          self.combopriceI.config(value=self.price_dals)
          self.combopriceI.current(0)
          self.qty1.set(1)
        
       if self.combosubcategI.get()=="Mustard":
          self.combopriceI.config(value=self.price_mus)
          self.combopriceI.current(0)
          self.qty1.set(1)
        
       if self.combosubcategI.get()=="Fenugreek":
          self.combopriceI.config(value=self.price_fenu)
          self.combopriceI.current(0)
          self.qty1.set(1)
        
       if self.combosubcategI.get()=="Rava":
          self.combopriceI.config(value=self.price_rava)
          self.combopriceI.current(0)
          self.qty1.set(1)
        
       if self.combosubcategI.get()=="Barley":
          self.combopriceI.config(value=self.price_barley)
          self.combopriceI.current(0)
          self.qty1.set(1)
        
       if self.combosubcategI.get()=="Nuts":
          self.combopriceI.config(value=self.price_nuts)
          self.combopriceI.current(0)
          self.qty1.set(1)
        
       if self.combosubcategI.get()=="Sugar":
          self.combopriceI.config(value=self.price_sugar)
          self.combopriceI.current(0)
          self.qty1.set(1) 
       
       if self.combosubcategI.get()=="Chana":
          self.combopriceI.config(value=self.price_chana)
          self.combopriceI.current(0)
          self.qty1.set(1)
        
       if self.combosubcategI.get()=="Pepper":
          self.combopriceI.config(value=self.price_Pepper)
          self.combopriceI.current(0)
          self.qty1.set(1)
        
       if self.combosubcategI.get()=="Jeera":
          self.combopriceI.config(value=self.price_Jeera)
          self.combopriceI.current(0)
          self.qty1.set(1)

       if self.combosubcategI.get()=="Clove":
          self.combopriceI.config(value=self.price_Clove)
          self.combopriceI.current(0)
          self.qty1.set(1)
        
       if self.combosubcategI.get()=="Poppy":
          self.combopriceI.config(value=self.price_Poppy)
          self.combopriceI.current(0)
          self.qty1.set(1)
        #
       if self.combosubcategI.get()=="Sambar Powder":
          self.combopriceI.config(value=self.price_sambarpowder)
          self.combopriceI.current(0)
          self.qty1.set(1) 
       if self.combosubcategI.get()=="Chilli Powder":
          self.combopriceI.config(value=self.price_chilli)
          self.combopriceI.current(0)
          self.qty1.set(1)
        
       if self.combosubcategI.get()=="Coriender Powder":
          self.combopriceI.config(value=self.price_coriender)
          self.combopriceI.current(0)
          self.qty1.set(1)
        
       if self.combosubcategI.get()=="Turmeric Powder":
          self.combopriceI.config(value=self.price_Turmeric)
          self.combopriceI.current(0)
          self.qty1.set(1)        
        #
       if self.combosubcategI.get()=="Milk powder":
          self.combopriceI.config(value=self.price_milk)
          self.combopriceI.current(0)
          self.qty1.set(1)
        
       if self.combosubcategI.get()=="Ghee":
          self.combopriceI.config(value=self.price_ghee)
          self.combopriceI.current(0)
          self.qty1.set(1)
        
       if self.combosubcategI.get()=="Butter":
          self.combopriceI.config(value=self.price_butter)
          self.combopriceI.current(0)
          self.qty1.set(1) 

       if self.combosubcategI.get()=="Paneer":
          self.combopriceI.config(value=self.price_paneer)
          self.combopriceI.current(0)
          self.qty1.set(1)
        
    def categories2(self,event=""):
        if self.combocategII.get()=="Medical products":
           self.combosubcategII.config(value=self.subcategmedi_products)
           self.combosubcategII.current(0)
        if self.combosubcategII.get()=="Select option":
          self.combopriceII.set(0)

        if self.combocategII.get()=="Bags":
           self.combosubcategII.config(value=self.subcategbags)
           self.combosubcategII.current(0)
        if self.combosubcategII.get()=="Select option":
          self.combopriceII.set(0)
        
        if self.combocategII.get()=="Stationary":
           self.combosubcategII.config(value=self.subacategstationary)
           self.combosubcategII.current(0)
        if self.combosubcategII.get()=="Select option":
          self.combopriceII.set(0)
        
        if self.combocategII.get()=="Others":
           self.combosubcategII.config(value=self.subcategothers)
           self.combosubcategII.current(0)
        if self.combosubcategII.get()=="Select option":
          self.combopriceII.set(0)
    
    def prod_price2(self,event=""):

       if  self.combosubcategII.get()=="boroline":
           self.combopriceII.config(value=self.price_boroline)
           self.combopriceII.current(0)
           self.qty2.set(1)

       if  self.combosubcategII.get()=="cotton":
           self.combopriceII.config(value=self.price_cotton)
           self.combopriceII.current(0)
           self.qty2.set(1)
       if  self.combosubcategII.get()=="Bandage":
           self.combopriceII.config(value=self.price_bandage)
           self.combopriceII.current(0)
           self.qty2.set(1)
       if  self.combosubcategII.get()=="Detol":
           self.combopriceII.config(value=self.price_detol)
           self.combopriceII.current(0)
           self.qty2.set(1)
       if  self.combosubcategII.get()=="volinispray":
           self.combopriceII.config(value=self.price_volini)
           self.combopriceII.current(0)
           self.qty2.set(1)
      #bags
       if  self.combosubcategII.get()=="School bags":
           self.combopriceII.config(value=self.price_schoolbags)
           self.combopriceII.current(0)
           self.qty2.set(1)
       if  self.combosubcategII.get()=="Luggage Bags":
           self.combopriceII.config(value=self.price_lugg)
           self.combopriceII.current(0)
           self.qty2.set(1)
       if  self.combosubcategII.get()=="Handbags":
           self.combopriceII.config(value=self.price_handbags)
           self.combopriceII.current(0)
           self.qty2.set(1)
       #stationary
       if  self.combosubcategII.get()=="Books":
           self.combopriceII.config(value=self.price_books)
           self.combopriceII.current(0)
           self.qty2.set(1)
       if  self.combosubcategII.get()=="A4 sheets":
           self.combopriceII.config(value=self.price_A4)
           self.combopriceII.current(0)
           self.qty2.set(1)
       if  self.combosubcategII.get()=="Pens":
           self.combopriceII.config(value=self.price_pens)
           self.combopriceII.current(0)
           self.qty2.set(1)
       if  self.combosubcategII.get()=="Sketches":
           self.combopriceII.config(value=self.price_sketches)
           self.combopriceII.current(0)
           self.qty2.set(1)
       if  self.combosubcategII.get()=="Pencils":
           self.combopriceII.config(value=self.price_pencil)
           self.combopriceII.current(0)
           self.qty2.set(1)
      #others
       if  self.combosubcategII.get()=="Cool Drinks":
           self.combopriceII.config(value=self.price_col)
           self.combopriceII.current(0)
           self.qty2.set(1)
       if  self.combosubcategII.get()=="Chocolates":
           self.combopriceII.config(value=self.price_choco)
           self.combopriceII.current(0)
           self.qty2.set(1)
       if  self.combosubcategII.get()=="Snacks":
           self.combopriceII.config(value=self.price_snacks)
           self.combopriceII.current(0)
           self.qty2.set(1)
            

if __name__=='__main__':
    root=Tk()
    obj=Bill_app(root)
    root.mainloop( )