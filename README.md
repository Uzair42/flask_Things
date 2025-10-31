<h1> Python ki web development ki liberary k bary main kuch aham chezy...</h1>

 ye ik lightweight libarary hy jo web deveolpment k choty projects or micro-services ki liye best hy,  
iss main routs ki basic functionality majood hy oor sath main template render ki bi ,  
jo k web dev main tazi oor asani paida karti hy   

---

sab sy pahly tu aap ny flask ko install karna hy   
linux ki liye pahly aap virtual envirment bana ly 
```python
 pip install flask
  ```

aab file create kar k uss ka name likh ,   
 Flask class import kary
```python
 from flask import Flask
  ```
  ***

Flask class ka ik object ya instance banay 
 variable __app__ ye flask class ka instance hy jo  
  - incoming Web Request 
  - Routes
  - Configure the application
  - etc 
kamo ka zimdar hota hy

``` python
app = Flask (__name__)
```

 __"__name__"__ ik asa varible hy jo current module ka naam save karta hy  
 agar tu aap is file ko direct run karty hn tu ye "main" ki value set kary ga  
 Agar aap iss kis oor file main import karty hn Tu ye ussi file module name ko store kary ga  
  <h4>is sy flask ko root directory ka ilam ho jata hy, Jo iss ko Dosry Static Resources ki location ko maloom kaarny main help karta hy</h4>
***
