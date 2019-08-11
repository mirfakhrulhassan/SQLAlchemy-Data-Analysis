from flask import Flask, jsonify
from sqlalchemy import create_engine,inspect,func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
import datetime as dt
from sqlalchemy import Date, cast
from datetime import datetime

engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)


app = Flask(__name__)
Measurement = Base.classes.measurement
Station = Base.classes.station

@app.route('/')
def index():
    return("Welcome:  <br/>  " 
    " Available routes: <br/> "
    "/api/v1.0/precipitation <br/> "
    "/api/v1.0/stations <br/> "
    "/api/v1.0/tobs  <br/> "
    "/api/v1.0/start  <br/> "
    "/api/v1.0/start/end <br/> "
    
    )


@app.route('/api/v1.0/tobs')   
def tbs():
    session = Session(engine)
    last_data_point = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    daate = last_data_point[0]
    dtt = datetime.strptime(last_data_point[0],'%Y-%m-%d')
    Last_year_date = dt.date(dtt.year,dtt.month,dtt.day)-dt.timedelta(days =365)
    temps = session.query(Measurement.date,Measurement.tobs).filter(Measurement.date>=Last_year_date).filter(Measurement.date<=daate).filter(Station.station == Measurement.station).filter(Station.station == 'USC00519281').all()
    
    
    
    lst_prc=[]
    for temp in temps:
        perc_dict = {}
        perc_dict["Date"] = temp[0]
        perc_dict['Temp'] = temp[1]
        lst_prc.append(perc_dict)

    return jsonify(lst_prc)

@app.route('/api/v1.0/stations')
def sttns():
    session = Session(engine)

    return jsonify(session.query(Station.station).all())

@app.route('/api/v1.0/precipitation')   
def prcptn():
    session = Session(engine)

    temps1 = session.query(Measurement.date,Measurement.prcp).filter(Station.station == Measurement.station).all()
    
        
    lst_prc1=[]
    for temp1 in temps1:
        perc_dict1 = {}
        perc_dict1["date"] = temp1[0]
        perc_dict1['prcp'] = temp1[1]
        lst_prc1.append(perc_dict1)

    return jsonify(lst_prc1)


    

@app.route('/api/v1.0/<start>')
def strt(start):
    session = Session(engine)
    s = jsonify(session.query(func.min(Measurement.tobs),func.avg(Measurement.tobs),func.max(Measurement.tobs)).filter(Measurement.date>=start).all())
    #session.remove()
    return s
    

@app.route('/api/v1.0/<begin>/<end>')
def st_end(begin,end):
     session = Session(engine)

     st_end1 = session.query(func.min(Measurement.tobs),func.avg(Measurement.tobs),func.max(Measurement.tobs)).filter(Measurement.date>=begin).filter(Measurement.date<=end).all()
     return jsonify(st_end1)

if __name__ == "__main__":
    app.run(debug = True)