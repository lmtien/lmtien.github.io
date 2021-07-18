---
title: "Single Responsibility Principle (SRP)"
categories:
  - Software-Development
tags:
  - backend
---

We have learnt Object-oriented programming (OOP) in school or have some experiences while working as developers, however not everyone can apply OOP properly and logically. 

SOLID is an acronym for the first five object-oriented design (OOD) principles by Robert C. Martin (also known as Uncle Bob). SOLID appears to be one of directions which helps developers design and implement system with higher quality: clean code, extendable, easy maintenance, etc.

SOLID stands for:
- `S` - Single Responsibility principle.
- `O` - Open-Closed principle.
- `L` - Liskov substitution principle.
- `I` - Interface segregation principle.
- `D` - Dependency inversion principle.

In this article, I will talk about the Single Responsibility Principle (SRP).

## What does it state?

> A class should have one and only one reason to change, meaning that a class should have only one job.

In short, this principle talks about *single responsibility* (as its name). For example, if you are a software developer then you should focus on coding or software related tasks; other tasks or jobs such as admin, office supplies, cleaning, financing, etc. will be managed by other people. Divide tasks base on the knowledge in a particular field will help to increase to increase the productivity and quality. (Because other people are more expertise than yourself in their areas).

This principle is not only applied to IT but also to almost all areas in our life: Focus on your expertise, if you spread yourself into too many different fields, the outcome will not be good.

![image-center](/assets/images/post/2021-07-17-single-responsibility.png){: .align-center}

Let’s look at the picture above and think about it. With your limited time available per day, if you need to do your main job as the main income to support your family, at the same time, you still need to take care of your babies, cooking, washing, cleaning, etc. There is high chance that you would not be able to complete any tasks or jobs well.

If you want the job to be finished with high quality, try to break it into smaller tasks, and assign them to other family members, hire helper, nanny. Then you can focus on your main job with high productivity.

## How to apply the SRP principle?

In software development, when you design a system with the ease of maintainability and Extensibility, you should design with the direction of single responsibility: each class or module should only be responsible for only one function. If there is a code which is not belong to class’ responsibility, then you need to separate it to other classes.

Let’s take one example below, we have a Student class with some simple methods such as get student information, submit or apply for scholarship, etc.

```c#
class Student
{
   private string name;
   private int age;
 
   string getStudentInfoJson()
   {
      return json_encode( array(name, age) );
   }
 
   string getStudentInfoHtml()
   {
      return "<span> Name: " + name + ", age: " + age + "</span>";
   }
 
   int applyForScholarship()
   {
      try
      {
         // Trying to apply for scholarship
      }
      catch
      {
         //write error to log file
         system.Out.print("Error_log.txt", "Error getting scholarship!");
      }
   }
}
```

Is that design or above class okay for long run?

Of course, that class can be used and runnable with correct output. However, it seems Student class is taking care of too many different works: provide student’s information, formatting the information, writing logs, apply scholarship, etc.

That means it is violating the single responsibility principle. Logically, we can ask ourselves few questions: why student needs to format the data? What if we want to write log from file to database? How can we modify code if we want to change log formatting? etc.

Using SOLID principles, it will be better if we design separated classes for data formatting and writing log. We can refactor the code above with the following:

```c#
class Student
{
   private string name;
   private int age;
 
   string getName()
   {
      return name;
   }
 
   int getName()
   {
      return age;
   }
 
   bool applyForScholarship()
   {
      try
      {
         // do something here
      }
      catch
      {
         ExportLog log_control = new ExportLog();
         log_control.exportLogToFile( "error_log.txt", "Error getting scholarship");
      }
   }
}
 
class Formatter()
{
   string formatInfoJson(string name, int age)
   {
      return json_encode( array( name, age ) );
   }
 
   string getStudentInfoHtml(string name, int age)
   {
      return "<span> Name: " + name + ", age: " + age + "</span>";
   }
}
 
class ExportLog
{
   void exportLogToFile(string filename, string error)
   {
      //write error to log file
      system.Out.print( filename, error );
   }
}
```

As you can see, by separating the responsibilities makes our code cleaner, easier to read, maintain and extend. It can be adapted with other ways of formatting in the future or it can provide many ways for exporting logs when the application grows bigger.

## Conclusion

Although the SRP may look simply, but reality we need to spend lots of time for practice in order to be master this principle. Technically, the class above can also be improved better if we apply other principle of SOLID, but this time, we only talk about SRP.

> You can look at [this comprehensive article](https://www.digitalocean.com/community/conceptual_articles/s-o-l-i-d-the-first-five-principles-of-object-oriented-design) for complete SOLID explanations.
