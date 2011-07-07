import asciitable

ipac_reader = asciitable.get_reader(Reader=asciitable.Ipac)
ipac_table = ipac_reader.read('t/ipac.dat')

cds_writer = asciitable.get_writer(Writer=asciitable.Cds)
asciitable.write(ipac_reader,'t/ipac_convert_to_cds.cds',Writer=asciitable.Cds)
#cds_writer.write(table=ipac_reader)

