"""
The code is very simple to run, it just requires a working terminal such as MacOS' terminal or Windows Putty and the ability to run python scripts. The first step is to create a file in the working directory called 'Censys_Certificates.txt' where the csv will be written onto. After that by using your own api_id and api_secret id which can be changed in the code, you can run the code using 'python Censys.py'and the textfile that you created above will now have a csv of the SHA256 fingerprints and the certificates start and end dates on their validity.
"""

from censys.search import CensysCertificates
import csv

c = CensysCertificates(
  api_id="d58fb70f-6082-4879-82ed-096953fe6286",
  api_secret="bSDw8UL0zr7byH0xSrrxVGcpK8p36yov"
)

#Queries the certificates that are trusted from censys.io
query = c.search("parsed.names:censys.io and tags: trusted")

with open ('Censys_Certificates.txt', 'w') as csv_file:
    fieldnames = ['SHA256_fingerprints', 'validity_start', 'validity_end']
    writer = csv.writer(csv_file)

    writer.writerow(fieldnames)
    for line in query:
        #Views the details of the certificate with the given SHA256 fingerprint for the validity start and end dates
        view = c.view(line['parsed.fingerprint_sha256'])
        writer.writerow([line['parsed.fingerprint_sha256'], view['parsed']['validity']['start'], view['parsed']['validity']['end']])
        
print("The process is complete, check the file Censys_Certificates.txt to see the csv!")