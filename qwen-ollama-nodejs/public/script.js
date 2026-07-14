async function test(){
   const r = await fetch('http://localhost:3000/chinthaka');

   const x = await r.text();
   alert(x);
}