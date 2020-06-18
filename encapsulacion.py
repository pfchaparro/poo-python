# -*- coding: utf-8 -*-

class CasillaVotacion:

    def __init__(self, id, pais):
        self._id = id
        self._pais = pais
        self._region = None

    @property
    def region(self):# definimos método para la región (Función getter)
        return self._region

    @region.setter # definimos método para cambiar la región (Función setter)
    def region(self, region):
        if region in self._pais:
            self._region = region
        else:
            raise ValueError(f'la region {region} no es valida en {self._pais}')

#Instanciamos
casilla = CasillaVotacion(123, ['MexicoDF','Morelos'])
casilla.region = 'MexicoDF'
print(casilla.region)