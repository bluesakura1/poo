#ifndef CURSO_H
#define CURSO_H
#include <stdlib.h>
#include <iostream>
#include <list>


#include "estudiante.h"
#include "profesor.h"


using namespace std;

class curso
{
	public:
		profesor Profesor_asignado;
		list<estudiante> estudiantes;
		
		void editar_profesor();
	protected:
};


void curso::editar_profesor(profesor newprof){
	int prof;
	cout << "si desea cambiar de profesor precione 1, si no lo desea precione 0"<<"\n";
	cin >> prof;
	
	if (prof==1){
		Profesor_asignado = newprof;
	};
}



#endif
