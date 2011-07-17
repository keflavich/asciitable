"""
Test case for CDS table writing

Reads in an IPAC table and writes it out as a CDS table
Unfortunately, as of 7/7/11, IPAC tables do not have a 'descr' attribute
"""
import asciitable

# Generate an IPAC reader object
ipac_reader = asciitable.get_reader(Reader=asciitable.Ipac)
# Fill the IPAC reader from a table...
ipac_table = ipac_reader.read('t/ipac2.dat')

# create a CDS object
cds_writer = asciitable.get_writer(Writer=asciitable.Cds)
# write the ipac_reader Table using the CDS writer
# (I think there should be a wrapper for this...)
asciitable.write(ipac_reader,'t/ipac_convert_to_cds.cds',Writer=asciitable.Cds)


cds_reader = asciitable.get_reader(Reader=asciitable.Cds)
cds_table = cds_reader.read('t/cds2.dat')
asciitable.write(cds_reader,'t/cds_convert_to_cds.cds',Writer=asciitable.Cds)


test_read_ipaccds = cds_reader.read('t/ipac_convert_to_cds.cds')
print test_read_ipaccds
test_read_cdscds = cds_reader.read('t/cds_convert_to_cds.cds')
print test_read_cdscds[:5]
