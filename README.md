# Surfs Up!

Technology Used: SQLAlchemy, Pandas, Matplotlib and Flask

Summary:

![surfs-up.jpeg](Images/surfs-up.png)

Congratulations! To help with trip planning, some climate analysis are donte on the area. The following outlines what are done.

## Step 1 - Climate Analysis and Exploration

To begin, Python and SQLAlchemy were used to do basic climate analysis and data exploration of climate database. All of the following analysis were completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.

* Chose a start date and end date . 

* Used SQLAlchemy `create_engine` to connect tosqlite database.

* Used SQLAlchemy `automap_base()` to reflect ables into classes and save a reference to those classes called `Station` and `Measurement`.

### Precipitation Analysis

* Designed a query to retrieve the last 12 months of precipitation data.

* Selected only the `date` and `prcp` values.

* Loaded the query results into a Pandas DataFrame and set the index to the date column.

* Sorted the DataFrame values by `date`.

* Plotted the results using the DataFrame `plot` method.

  ![precipitation](Images/precipitation.png)

* Used Pandas to print the summary statistics for the precipitation data.

### Station Analysis

* Designed a query to calculate the total number of stations.

* Designed a query to find the most active stations.

  * Listed the stations and observation counts in descending order.

  * Found the station which has the highest number of observations.

  * Designed a query to retrieve the last 12 months of temperature observation data (tobs).

  * Filtered by the station with the highest number of observations.

  * Plotted the results as a histogram with `bins=12`.

    ![station-histogram](Images/station-histogram.png)

- - -

## Step 2 - Climate App

Designed a Flask API based on the queries that you have just developed.

* Used FLASK to create routes.

### Routes

* `/`

  * Home page.

  * List all routes that are available.

* `/api/v1.0/precipitation`

  * Converted the query results to a Dictionary using `date` as the key and `prcp` as the value.

  * Returned the JSON representation of your dictionary.

* `/api/v1.0/stations`

  * Returned a JSON list of stations from the dataset.

* `/api/v1.0/tobs`
  * query for the dates and temperature observations from a year from the last data point.
  * Returned a JSON list of Temperature Observations (tobs) for the previous year.

* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`

  * Returned a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

  * When given the start only, calculated `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.

  * When given the start and the end date, calculated the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.


