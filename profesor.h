#ifndef PROFESOR_H
#define PROFESOR_H
#include <stdlib.h>
#include <iostream>
#include <list>

#include "curso.h"

using namespace std;
class profesor
{
	public:
		string Name;
		int Id;
		int edad;
		list<curso> cursos;
		void estudiantes();
		
		
		void change_Name(string newname);
		void change_Id(int newid);
		void change_edad(int newedad);
		void change_cursos();
		
		
	protected:
};

void profesor::change_Name(string newname){
	Name = newname;	
}

void profesor::change_Id(int newid){
	Id=newid;
}

void profesor::change_edad(int newedad){
	edad=newedad;
}

void profesor::change_cursos(){
	int iter;
	int counter=0;
	cout << "si desea agregar un curso escriba 0, si desea salir ingrese 1  "<<"\n";
	cin >> iter;
	while(iter==0){
		
		curso cursoiter = cursos[0];
		cout << "desea cambiar el curso  "<< <<"\n";
	    cin >> iter;
		
		counter =counter+1;
	};

}


#endif
