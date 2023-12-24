from flask import Flask , request , render_template
import os
import sqlite3



app = Flask(__name__)

picFolder = os.path.join('static' ,'pics')

app.config['UPLOAD_FOLDER'] = picFolder

#Abdelhamid
pathy=os.path.dirname(os.path.abspath(__file__))
DATABASE= pathy +"/database/buses.db"


@app.route("/home")
def home():
    return render_template("land.html" )

@app.route("/success")
def success():
    return render_template("success.html" )

@app.route("/search")
def search():
    return render_template("search.html" )

@app.route("/result")
def result():
    return render_template("result.html"   )

@app.route("/add")
def add():
    return render_template("add.html"  )

@app.route("/about")
def about():
    return render_template("about.html"  )

@app.route("/details")
def details():
    return render_template("details.html"   )

@app.route("/footer")
def footer():

    return render_template("footer.html"  )



@app.route("/select" , methods=["POST" , "GET"])
def select():
    from_d = request.form.get("from")
    to_d = request.form.get("to")
    num = request.form.get("num")
    conn = sqlite3.connect(DATABASE) #abdelhmaid
    cur = conn.cursor()
    if num != "" :
        cur.execute(f"""SELECT Bus_nm , Direction
  FROM buses where Direction Like '{from_d}%' and Direction Like '%{to_d}%' and Bus_nm like '%{num}%';
                
                    """)
    else:
      cur.execute(f"""SELECT Bus_nm , Direction
  FROM buses where Direction Like '{from_d}%' and Direction Like '%{to_d}%';
                
                    """)
           
        
    
    conn.commit()
    result = cur.fetchall()
    

    len(result)
    conn.close()
    finalResult=[]
    for i in range(len(result)):
        d = {"busNumber" : result[i][0] , "busDirc" : result[i][1] }
        finalResult.append(d)
    leng = len(result)
    return render_template("result.html" , result = finalResult , leng = leng , from1 = from_d , to1 = to_d , num = num )




@app.route("/post" , methods=["POST" , "GET"])
def post():
    direct = request.form.get("direc")
    num = request.form.get("num")
    conn = sqlite3.connect(DATABASE) #abdelhmaid
    cur = conn.cursor()
    cur.execute(f"""SELECT Bus_nm 
  FROM buses where Bus_nm = {num};            
                    """)

           
        
    
    conn.commit()
    result = cur.fetchall()
    print(result)
    
    if result == []:
      cur.execute(f"""INSERT INTO buses (
                      Direction,
                      Bus_nm
                  )
                  VALUES (
                      '{direct}',
                      '{num}'
                  );
                  """)
    
      conn.commit()
      conn.close()
      return render_template("success.html" )
    else:
        return render_template("failed.html"  )
        
      
      
    
    
    
    
    













if __name__ == "__main__":
    app.run(debug=True )
