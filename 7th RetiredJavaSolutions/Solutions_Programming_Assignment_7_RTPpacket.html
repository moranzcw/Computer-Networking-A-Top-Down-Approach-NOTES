<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3c.org/TR/1999/REC-html401-19991224/loose.dtd">
<!-- saved from url=(0070)http://media.pearsoncmg.com/aw/aw_kurose_network_2/labs/RTPpacket.html -->
<HTML><HEAD><TITLE>RTPpacket.java</TITLE>
<META http-equiv=Content-Type content="text/html; charset=windows-1252">
<STYLE type=text/css>H1 {
	FONT-WEIGHT: normal; FONT-SIZE: 19pt; COLOR: #8989db; FONT-FAMILY: Arial, sans-serif
}
H2 {
	FONT-WEIGHT: bold; FONT-SIZE: 16pt; COLOR: black; FONT-FAMILY: Arial, sans-serif
}
H3 {
	FONT-WEIGHT: bold; FONT-SIZE: 14pt; COLOR: #8989db; FONT-FAMILY: Arial, sans-serif
}
P {
	FONT-SIZE: 10pt; FONT-FAMILY: Arial, sans-serif
}
TD {
	FONT-SIZE: 10pt; FONT-FAMILY: Arial, sans-serif
}
TH {
	FONT-SIZE: 10pt; FONT-FAMILY: Arial, sans-serif
}
DT {
	FONT-SIZE: 10pt; FONT-FAMILY: Arial, sans-serif
}
DD {
	FONT-SIZE: 10pt; FONT-FAMILY: Arial, sans-serif
}
LI {
	FONT-SIZE: 10pt; FONT-FAMILY: Arial, sans-serif
}
A:link {
	COLOR: #000066
}
A:visited {
	COLOR: #666666
}
</STYLE>

<META content="MSHTML 6.00.2800.1400" name=GENERATOR></HEAD>
<BODY>
<H3><A name=rtppacket>RTPpacket.java</A></H3><PRE>//class RTPpacket

public class RTPpacket{

  //size of the RTP header:
  static int HEADER_SIZE = 12;

  //Fields that compose the RTP header
  public int Version;
  public int Padding;
  public int Extension;
  public int CC;
  public int Marker;
  public int PayloadType;
  public int SequenceNumber;
  public int TimeStamp;
  public int Ssrc;
  
  //Bitstream of the RTP header
  public byte[] header;

  //size of the RTP payload
  public int payload_size;
  //Bitstream of the RTP payload
  public byte[] payload;
  


  //--------------------------
  //Constructor of an RTPpacket object from header fields and payload bitstream
  //--------------------------
  public RTPpacket(int PType, int Framenb, int Time, byte[] data, int data_length){
    //fill by default header fields:
    Version = 2;
    Padding = 0;
    Extension = 0;
    CC = 0;
    Marker = 0;
    Ssrc = 0;

    //fill changing header fields:
    SequenceNumber = Framenb;
    TimeStamp = Time;
    PayloadType = PType;
    
    //build the header bistream:
    //--------------------------
    header = new byte[HEADER_SIZE];

    //.............
    //TO COMPLETE
    //.............
    //fill the header array of byte with RTP header fields

    //header[0] = ...
    // .....
 

    //fill the payload bitstream:
    //--------------------------
    payload_size = data_length;
    payload = new byte[data_length];

    //fill payload array of byte from data (given in parameter of the constructor)
    //......

    // ! Do not forget to uncomment method printheader() below !

  }
    
  //--------------------------
  //Constructor of an RTPpacket object from the packet bistream 
  //--------------------------
  public RTPpacket(byte[] packet, int packet_size)
  {
    //fill default fields:
    Version = 2;
    Padding = 0;
    Extension = 0;
    CC = 0;
    Marker = 0;
    Ssrc = 0;

    //check if total packet size is lower than the header size
    if (packet_size &gt;= HEADER_SIZE) 
      {
	//get the header bitsream:
	header = new byte[HEADER_SIZE];
	for (int i=0; i &lt; HEADER_SIZE; i++)
	  header[i] = packet[i];

	//get the payload bitstream:
	payload_size = packet_size - HEADER_SIZE;
	payload = new byte[payload_size];
	for (int i=HEADER_SIZE; i &lt; packet_size; i++)
	  payload[i-HEADER_SIZE] = packet[i];

	//interpret the changing fields of the header:
	PayloadType = header[1] &amp; 127;
	SequenceNumber = unsigned_int(header[3]) + 256*unsigned_int(header[2]);
	TimeStamp = unsigned_int(header[7]) + 256*unsigned_int(header[6]) + 65536*unsigned_int(header[5]) + 16777216*unsigned_int(header[4]);
      }
 }

  //--------------------------
  //getpayload: return the payload bistream of the RTPpacket and its size
  //--------------------------
  public int getpayload(byte[] data) {

    for (int i=0; i &lt; payload_size; i++)
      data[i] = payload[i];

    return(payload_size);
  }

  //--------------------------
  //getpayload_length: return the length of the payload
  //--------------------------
  public int getpayload_length() {
    return(payload_size);
  }

  //--------------------------
  //getlength: return the total length of the RTP packet
  //--------------------------
  public int getlength() {
    return(payload_size + HEADER_SIZE);
  }

  //--------------------------
  //getpacket: returns the packet bitstream and its length
  //--------------------------
  public int getpacket(byte[] packet)
  {
    //construct the packet = header + payload
    for (int i=0; i &lt; HEADER_SIZE; i++)
	packet[i] = header[i];
    for (int i=0; i &lt; payload_size; i++)
	packet[i+HEADER_SIZE] = payload[i];

    //return total size of the packet
    return(payload_size + HEADER_SIZE);
  }

  //--------------------------
  //gettimestamp
  //--------------------------

  public int gettimestamp() {
    return(TimeStamp);
  }

  //--------------------------
  //getsequencenumber
  //--------------------------
  public int getsequencenumber() {
    return(SequenceNumber);
  }

  //--------------------------
  //getpayloadtype
  //--------------------------
  public int getpayloadtype() {
    return(PayloadType);
  }


  //--------------------------
  //print headers without the SSRC
  //--------------------------
  public void printheader()
  {
    //TO DO: uncomment
    /*
    for (int i=0; i &lt; (HEADER_SIZE-4); i++)
      {
	for (int j = 7; j&gt;=0 ; j--)
	  if (((1&lt;&lt;j) &amp; header[i] ) != 0)
	    System.out.print("1");
	else
	  System.out.print("0");
	System.out.print(" ");
      }

    System.out.println();
    */
  }

  //return the unsigned value of 8-bit integer nb
  static int unsigned_int(int nb) {
    if (nb &gt;= 0)
      return(nb);
    else
      return(256+nb);
  }

}
</PRE></BODY></HTML>
