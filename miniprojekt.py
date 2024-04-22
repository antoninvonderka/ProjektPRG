import aspose.pdf as pdf
import aspose.pydrawing as drawing

filePath = "C://Words//"

pdfCropLicense = pdf.License()

pdfCropLicense.set_license(filePath + "Conholdate.Total.Product.Family.lic")

pdfDoc = pdf.Document(filePath + "GeneratedPdf.pdf")

signature = pdf.facades.PdfFileSignature(pdfDoc)

pkcs = pdf.forms.PKCS7(filePath + "sample.pfx", "123456789")

docMdpSignature = pdf.forms.DocMDPSignature(pkcs, pdf.forms.DocMDPAccessPermissions.FILLING_IN_FORMS)

rect = drawing.Rectangle(150, 650, 450, 150)
signature.signature_appearance = "sample.jpg"

signature.certify(1, "Signature Insert  Reason", "Contact", "Location", True, rect, docMdpSignature)

signature.save("Digitally Signed PDF.pdf")
