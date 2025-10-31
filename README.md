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

<h2>Flask Instance </h2>
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

 __naame__ ik asa varible hy jo current module ka naam save karta hy  
 agar tu aap is file ko direct run karty hn tu ye "main" ki value set kary ga  
 Agar aap iss kis oor file main import karty hn Tu ye ussi file module name ko store kary ga  
  <h4>is sy flask ko root directory ka ilam ho jata hy, Jo iss ko Dosry Static Resources ki location ko maloom kaarny main help karta hy</h4>

***

<h2>Routes</h2>
 Routing flask main appko route() k zariye hoti hy iss main aap url route ka bato   
 python main function define karo jo return kary respose    
 jab url parameter pass hoga tu , wo function ko as argument mily ga , jo baad main function logiv use hoga .  

 ```python
 # passing parameter in url 
@app.route('/student/<name>')
def Student_name(name):
        return f"Result of : {name} !"
```
<h2>Redirect</h2>
redirect karny k liye pahly flask sy redirect , oor url_for import karo 
```python
from flask import redirect ,url_for
```
redirect karny k lie return py redirect() main url_for() main wo function bato jis main app redirect karna chaty hn

```python
# Redirecting to Student Analytics Page
@app.route('/student')
def Student():
    if isLogin==False:
        return redirect(url_for("dashborad"))
    else :
        return "Student Analytics Page"
```



***


  
