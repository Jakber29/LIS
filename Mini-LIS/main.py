import sqlite3

def create_database():
    conn = sqlite3.connect('lis_system.db')
    cursor = conn.cursor()


    # Drop tables if they exist
    cursor.execute("DROP TABLE IF EXISTS SampleTechnicianLog")
    cursor.execute("DROP TABLE IF EXISTS Samples")
    cursor.execute("DROP TABLE IF EXISTS Technicians")
    cursor.execute("DROP TABLE IF EXISTS Patients")
    
    #Create Patients Table
    cursor.execute('''CREATE TABLE Patients (
                   PatientID INTEGER PRIMARY KEY,
                   FirstName TEXT,
                   LastName TEXT,
                   DateOfBirth TEXT,
                   Gender TEXT)''')
    #Create Samples Table
    cursor.execute('''CREATE Table Samples (
                   SampleID INTEGER PRIMARY KEY,
                   PatientID INTEGER,
                   DateCollected TEXT,
                   Type TEXT,
                   Status TEXT,
                   Results TEXT,
                   FOREIGN KEY(PatientID) REFERENCES Patients(PatientID))''')
    #Create Technicians Table
    cursor.execute('''CREATE TABLE Technicians (
                   TechID INTEGER PRIMARY KEY,
                   FirstName TEXT,
                   LastName TEXT,
                   Role TEXT)''')
    #Create SampleTechnicianLog Table
    cursor.execute('''CREATE TABLE SampleTechnicianLog (
                   LogID INTEGER PRIMARY KEY,
                   SampleID INTEGER,
                   TechID INTEGER
                   Date TEXT,
                   Action TEXT,
                   FOREIGN KEY(SampleID) REFERENCES Samples(SampleID),
                   FOREIGN KEY(TechID) REFERENCES Technicians(TechID))''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
