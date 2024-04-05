import psycopg2
from psycopg2.extras import Json
import json

# Configure your PostgreSQL connection parametres
db_params = {
    'host':'0.0.0.0',
    'database':'vedas_dataset_catelog',
    'user':'postgres',
    'password':'sac123',
    'port':5432
}

def connect_to_database():
    """Connect to PostgreSQL database."""
    try:
        connection = psycopg2.connect(**db_params)
        return connection
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None


def insert_data(name, metadata, id, source_location, temporal_frequency, extension, resampling, compression, interleave, projection, paused, band_info):
    """Data added from the form."""
    try:
        connection = connect_to_database()
        if connection:

            cursor = connection.cursor()

            info = ''
            start = True
            for e in band_info:
                if start:
                    start = False
                else:
                    info += ','
                info += "'" + str(json.dumps(e)) + "'::jsonb"

            # band_info_json = json.dumps(band_info)

            query_1 = "INSERT INTO datasets (name, metadata, id, source_location, temporal_frequency, extension, resampling, compression, interleave, band_info) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,ARRAY[" + info + "]) RETURNING id"
            cursor.execute(query_1, (name, json.dumps(metadata), id, source_location, temporal_frequency, extension, resampling, compression, interleave))
            dataset_id = cursor.fetchone()[0]

            
            for projection in projection:
                query_2 = "INSERT INTO pyramid_properties (dataset_id, projection, paused) VALUES (%s,%s,%s)"
                cursor.execute(query_2, (dataset_id, projection, paused))

            connection.commit()
            cursor.close()
            connection.close()
            return True
    except Exception as e:
        print(f"Error inserting data: {e}")
    return False




def get_data():
    """Fetch all data from datasets."""
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
         
            # query = """
            #     SELECT datasets.*, pyramid_properties.projection, pyramid_properties.paused 
            #     FROM datasets 
            #     INNER JOIN pyramid_properties ON datasets.id = pyramid_properties.dataset_id
            # """
            # cursor.execute(query)
            # rows = cursor.fetchall()
            # cursor.close()
            # connection.close()
            # return rows, cursor.description

            query = """
                SELECT datasets.*, array_agg(pyramid_properties.projection) AS projections, pyramid_properties.paused 
                FROM datasets 
                INNER JOIN pyramid_properties ON datasets.id = pyramid_properties.dataset_id
                GROUP BY datasets.id, datasets.name, datasets.metadata, datasets.source_location, datasets.temporal_frequency, 
                datasets.extension, datasets.resampling, datasets.compression, datasets.interleave, datasets.band_info, pyramid_properties.paused
            """
            cursor.execute(query)
            rows = cursor.fetchall()
            cursor.close()
            connection.close()
            return rows, cursor.description
        
    
    except Exception as e:
        print(f"Error fetching data: {e}")
    return None



def update(id,new_name,new_source_location,new_metadata):
    """Update the values from datasets."""
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            query = "UPDATE datasets SET name = %s, source_location = %s, metadata = %s WHERE id = %s"
            cursor.execute(query,(new_name,new_source_location,json.dumps(new_metadata),id))
            connection.commit()
            cursor.close()
            connection.close()
            return True
    except Exception as e:
        print(f"Error updating data: {e}")
    return False
