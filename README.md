# HackSI2018 (Merdian's Beacon)

Rails App used to send mass text messages ([textmagic-ruby](https://github.com/textmagic/textmagic-rest-ruby)), mass emails, and display an image on the web app whenever the beacon, which has sensors in it to identify it, gets touched. Other things that happen once the beacon is touched include updating [twitter](https://twitter.com/thebeacon10/), [instagram](https://www.instagram.com/thebeacon_hacksi/), and a speaker on the beacon all saying "A new hand touches the beacon".

**Ngrok**

It uses ngrok to proxy puma web server out to the web

```
$ ngrok http 127.0.0.1:3000
```

![Merdian's Beacon](https://survivinskyrim.files.wordpress.com/2015/11/morc16-8.jpg)
![Our Version](https://github.com/EasyIP2023/hacksi_2018/blob/master/IMG_20181103_193819.jpg)
