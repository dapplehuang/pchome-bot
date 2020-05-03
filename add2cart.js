var f = new URLSearchParams();

var formData = {
    "G":[],"A":[],"B":[],"TB":"24H","TP":2,"T":"ADD",
    "TI":"DGBJ88-A900A9ZHU-000",
    "RS":"",
    "YTQ": 1
  };

f.set('data', JSON.stringify(formData));

fetch('https://24h.pchome.com.tw/cart/index.php/prod/modify', {
  method: 'POST',
  body: f,
  headers: {
    // 'Content-type': 'application/json; charset=UTF-8'
  }
})
.then(res => res.json())
.then(console.log)