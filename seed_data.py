from ejemplo.models import Familiar
from blog.models import Post, Usuario


Familiar(nombre="Rosario", direccion="Rio Parana 745", numero_pasaporte=123123).save()
Familiar(nombre="Alberto", direccion="Rio Parana 745", numero_pasaporte=890890).save()
Familiar(nombre="Samuel", direccion="Rio Parana 745", numero_pasaporte=345345).save()
Familiar(nombre="Florencia", direccion="Rio Parana 745", numero_pasaporte=567567).save()

print("Se cargo con éxito los Familiares de pruebas")

print("Se cargo con éxito los Familiares de pruebas")



Post(title="Mi post CODEHOUSE", short_content="un post de CODEHOUSE", content="sadljalsjdlkajsdljasljdlaksjd").save()

print("Se cargo con éxito los post de pruebas")
