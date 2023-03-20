#                                               BİSMİLLAHİRRAHMANİRRAHİM


import vobject
import glob

def parse_vcard(path):
    allVCards = glob.glob(path)
    for i in allVCards:
        with open(i, 'r', encoding="utf-8") as f:
            vcard = vobject.readOne(f.read())
            write_to_vcf( {vcard.contents['fn'][0].value: [tel.value for tel in vcard.contents['tel']] } )

def process_name(name):
    return name.replace(" ", "=20").replace("Ç","=c3=87").replace("ç","=c3=a7").replace("Ğ","=c4=9e").replace("ğ","=c4=9f").replace("İ","=c4=b0").replace("ı","=c4=b1").replace("Ö","=c3=96").replace("ö","=c3=b6").replace("Ş","=c5=9e").replace("ş","=c5=9f").replace("Ü","=c3=9c").replace("ü","=c3=bc")

def write_to_vcf(vcard_fn):
    name=""
    
    for key in vcard_fn:
        name = key
        
    tel =vcard_fn[name][0]
    new_name = process_name(name)
    example_data = """BEGIN:VCARD
VERSION:2.1
N;ENCODING=QUOTED-PRINTABLE;CHARSET=UTF-8:""" + new_name + """;;;
TEL;CELL:""" + tel + """
X-CLASS:private
END:VCARD"""
    f = open("C:\\tests_2\\" + name + ".vcf","w")
    f.write(example_data)
    f.close()
    

parse_vcard("C:\\example_path\\*")
