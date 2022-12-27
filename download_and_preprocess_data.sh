mkdir download && cd download
mkdir {med,cacm,npl}

# download Medline
curl -O http://ir.dcs.gla.ac.uk/resources/test_collections/medl/med.tar.gz
tar -zxf med.tar.gz -C med/
rm med.tar.gz

# download CACM
curl -O http://ir.dcs.gla.ac.uk/resources/test_collections/cacm/cacm.tar.gz
tar -zxf cacm.tar.gz -C cacm/
rm cacm.tar.gz

# download NPL
curl -O http://ir.dcs.gla.ac.uk/resources/test_collections/npl/npl.tar.gz
tar -zxf npl.tar.gz -C npl/
rm npl.tar.gz

# convert datasets to JSON format
cd ..
python3 ./preprocessing.py

# clean
rm -rf download/
