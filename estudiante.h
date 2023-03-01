#ifndef ESTUDIANTE_H
#define ESTUDIANTE_H
#include <stdlib.h>
#include <iostream>
#include <list>


#include "profesor.h"
#include "curso.h"

using namespace std;
class estudiante
{
	public:
		string Name;
		int Id;
		int edad;
		list<curso> cursose;
		
		void change_Name(string newname);
		void change_Id(int newid);
		void change_edad(int newedad);
		void change_cursos();
		

};



void estudiante::change_Name(string newname){
	Name = newname;	
}

void estudiante::change_Id(int newid){
	Id=newid;
}

void estudiante::change_edad(int newedad){
	edad=newedad;
}


#endif
