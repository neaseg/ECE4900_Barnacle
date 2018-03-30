/********************************
 * This is a basic connectivity test of the nRF52. 
 * Advertises itself as hello_nRF52 at 115200 baud rate 
 * Next steps: Sending data back and forth
 ********************************/
#include <string.h>
#include <Arduino.h>
#include <bluefruit.h> 

// BLE Service
BLEUart bleuart;
BLEDis bledis;
BLEBas blebas;

#define STATUS_LED  (17)
#define BLINKY_MS   (2000)

uint32_t blinkyms;

void setup() {
  Serial.begin(115200);//baud rate
  Serial.println(F("nRF52 Controller Connection Example"));//not 100% sure what this does but this was included in the example code
  Serial.println(F("-----------------------------------"));//same with this line

  Bluefruit.begin();
  //accepted tx power values: -40, -30, -20, -16, -12, -8, -4, 0, 4
  //play around with and test this, very important to get this right
  Bluefruit.setTxPower(4);
  Bluefruit.setName("nRF52");
  Bluefruit.setConnectCallback(connect_callback);
  Bluefruit.setDisconnectCallback(disconnect_callback);

// Configure and Start Device Information Service
  bledis.setManufacturer("Adafruit Industries");
  bledis.setModel("Bluefruit Feather52");
  bledis.begin();

  //start BLE Uart service
  bleuart.begin();

  // Start BLE Battery Service
  blebas.begin();
  blebas.write(100);


  //Set up and begin advertising 
  startAdv();

  Serial.println(F("adv_line_1"));
  Serial.println(F("adv_line_1"));
  Serial.println();
}


//this part directly copy pasted from 
//https://github.com/adafruit/Adafruit_nRF52_Arduino/blob/master/libraries/Bluefruit52Lib/examples/Peripheral/controller/controller.ino
void startAdv(void)
{
  // Advertising packet
  Bluefruit.Advertising.addFlags(BLE_GAP_ADV_FLAGS_LE_ONLY_GENERAL_DISC_MODE);
  Bluefruit.Advertising.addTxPower();
  
  // Include the BLE UART (AKA 'NUS') 128-bit UUID
  Bluefruit.Advertising.addService(bleuart);

  // Secondary Scan Response packet (optional)
  // Since there is no room for 'Name' in Advertising packet
  Bluefruit.ScanResponse.addName();

  /* Start Advertising
   * - Enable auto advertising if disconnected
   * - Interval:  fast mode = 20 ms, slow mode = 152.5 ms
   * - Timeout for fast mode is 30 seconds
   * - Start(timeout) with timeout = 0 will advertise forever (until connected)
   * 
   * For recommended advertising interval
   * https://developer.apple.com/library/content/qa/qa1931/_index.html   
   */
  Bluefruit.Advertising.restartOnDisconnect(true);
  Bluefruit.Advertising.setInterval(32, 244);    // in unit of 0.625 ms
  Bluefruit.Advertising.setFastTimeout(30);      // number of seconds in fast mode
  Bluefruit.Advertising.start(0);                // 0 = Don't stop advertising after n seconds  
}



void loop() {
  // put your main code here, to run repeatedly:

  //sends 1 byte containing the number 8 every second over bluetooth
  bleuart.write(8);
  delay(1000);
}

void connect_callback(uint16_t conn_handle)
{
  char central_name[32] = { 0 };
  Bluefruit.Gap.getPeerName(conn_handle, central_name, sizeof(central_name));

  Serial.print("Connected to ");
  Serial.println(central_name);
}

void disconnect_callback(uint16_t conn_handle, uint8_t reason)
{
  (void) conn_handle;
  (void) reason;

  Serial.println();
  Serial.println("Disconnected");
}
