<script type="text/javascript">
let list_options = []

function SetQuery(pk){
  var query = pk
  // for(let p of list_options)
  for(var i=0; i<list_options.length;i++)
  {
    if (query == list_options[i])
    {
      // list_options.remove(query)
      list_options = list_options.splice(i, 1)

    }
    i++
  }
  list_options.push(query)
}
</script>
