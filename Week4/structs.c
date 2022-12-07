#include <stdio.h>
#include <string.h>
#include <stdlib.h>

struct Employee
{
    char *name;
    int age;
    double salary;
    int years_worked;
    char *job_title;
};

struct Module
{
    char name[50];
    int credits;
};

struct Student
{
    char name[10];
    int age;
    struct Module modules[10];
};

struct Manager
{
    char name[10];
    int age;
    double salary;
    struct Employee employee[10];
};

void printStudentInfo(struct Student student)
{
    printf("Student name is %s\nStudent age is %i\n",
           student.name, student.age);
};

void printEmployeeInfo(struct Employee employee)
{
    printf("Employee name is %s\nEmployee age is %u\nEmployee salary is %f\nYears worked = %u\nJob Title = %s",
           employee.name, employee.age, employee.salary, employee.years_worked, employee.job_title);
};

void printManagerInfo(struct Manager manager)
{
    printf("Manager name is %s\nManager age is %u\n", manager.name, manager.age);
};

void printEmployees(struct Employee employees)
{
    printf("The employee name is %s\n", employees.name);
};

void printModule(struct Module module)
{
    printf("the module name is %s\n", module.name);
};

int main(void)
{
    struct Student student = {"james", 23};
    struct Module module = {"Multi-paradigm Programming"};
    student.modules[0] = module;

    struct Module module2 = {"Economics"};
    student.modules[1] = module2;

    printModule(student.modules[0]);
    printModule(student.modules[1]);

    struct Manager manager = {"Rian", 45, 75000.00};
    struct Employee employee1 = {"Maeve", 28, 40000.00, 4, "Software Engineer"};
    manager.employee[0] = employee1;
    printEmployees(employee1);
};
