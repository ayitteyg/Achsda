

function SRCHfunction() {
  var input, filter, ul, li, a, i, txtValue;
  input = document.getElementById("srchInput");
  filter = input.value.toUpperCase();
  ul = document.getElementById("srchItem");
  li = ul.getElementsByTagName("li");
  for (i = 0; i < li.length; i++) {
      a = li[i].getElementsByTagName("a")[0];
      txtValue = a.textContent || a.innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
          li[i].style.display = "";
      } else {
          li[i].style.display = "none";
      }
  }
}



/*function to pass data to view*/
function getdata_in_view(url,dt){
  var url = url
    fetch(url,{
        method: 'POST',
        headers: {
         'Content-Type':'application/json',
         'X-CSRFToken':csrftoken},
         body:JSON.stringify({'dt':dt})             
    })
}




  function getToken(name) {
    let csrftoken = null;          
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();

            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                csrftoken = decodeURIComponent(cookie.substring(name.length + 1));

                break;
            }
        }
    }           
    return csrftoken;
  }
  var csrftoken = getToken('csrftoken')



