const int pinVoltaje = A0;                    // Pin para medir el voltaje
const int sensorPin = A5;                     // Pin analógico para el sensor de corriente
const int sensorPinTemA = A2;                 // Pin analógico para el sensor de temperatura del ánodo
const int sensorPinTemB = A3;                 // Pin analógico para el sensor de temperatura del cátodo
const float sensibilidad = 0.070;             // Sensibilidad del sensor de corriente (V/A)
const float factorConversion = 5.0 / 1023.0;  // Factor de conversión de ADC a voltaje
unsigned long tiempoAnterior = 0;             // Tiempo de la última lectura
float offset = 0.0;                           // Variable para almacenar el valor de offset

void setup() {
  Serial.begin(9600);                        
  obtenerOffset();                            // Llamar a la función para obtener el offset
}
void loop() {
  medirVoltaje();
  medirCorriente();
  medirTemperatura("A", sensorPinTemA);
  medirTemperatura("B", sensorPinTemB);
  delay(5000);
}
void medirVoltaje() {
  const int numReadings = 100;
  float totalVoltaje = 0.0;

  for (int i = 0; i < numReadings; i++) {
    int lectura = analogRead(pinVoltaje);
    float voltaje = lectura * factorConversion;
    totalVoltaje += voltaje;
  }
  float averageVoltaje = totalVoltaje / numReadings;
  Serial.print("Voltaje: ");
  Serial.println(averageVoltaje);
}
void medirCorriente() {
  const int numMediciones = 100;
  float sumaCorriente = 0.0;

  for (int i = 0; i < numMediciones; i++) {
    int lecturaADC = analogRead(sensorPin);
    float voltaje = lecturaADC * factorConversion;
    float corriente = (voltaje - offset) / sensibilidad;
    sumaCorriente += corriente;
  }
  float promedioCorriente = sumaCorriente / numMediciones;
  unsigned long tiempoActual = millis();
  float tiempoTranscurrido = (tiempoActual - tiempoAnterior) / 1000.0;
  Serial.print("Corriente: ");
  Serial.println(promedioCorriente, 3);
  tiempoAnterior = tiempoActual;
}
void medirTemperatura(const char* componente, int sensorPinTemp) {
  const int numReadings = 100;
  float totalTemperature = 0.0;

  for (int i = 0; i < numReadings; i++) {
    int sensorValue = analogRead(sensorPinTemp);
    float voltage = sensorValue * (5.0 / 1023.0);
    float temperature = (voltage - 0.5) * 100.0;
    totalTemperature += temperature;
  }
  float averageTemperature = totalTemperature / numReadings;
  Serial.print("Temperatura ");
  Serial.print(componente);
  Serial.print(": ");
  Serial.println(averageTemperature);
}
void obtenerOffset() {
  const int muestras = 100;
  float suma = 0.0;

  for (int i = 0; i < muestras; i++) {
    int lecturaADC = analogRead(sensorPin);
    suma += lecturaADC * factorConversion;
  }

  offset = suma / muestras;
}
