//Create a constructor function to be used in the end
function Suggest()
{
	console.log("JavaScript running")
	othis = this; //save this for future
	this.xhr = new XMLHttpRequest();
	this.read = null;
	
	this.div = null; //the container div
	
	//Create a timer (to decide when to go to server)
	this.timer = null;
	
	this.getBook = function()
	{
		if(this.timer)
		{
			clearTimeout(this.timer);
		}
		//Get ready to go to server in 1 second.
		// If the user types something before 1 second, this function
		// will be called and the timer is canceled before registering 
		// a new one. If the user keeps quiet for more than 1 second
		// then the fetchbooks function is called anyway
		
		this.timer = setTimeout(this.fetchBook, 1000);

	}
	
	//Function to check if we need to go to server or use cache data
	this.fetchBooks = function()
	{
		othis.read = document.getElementById("book");
		othis.div = document.getElementById("container");
		if(othis.read.value == "")
		{
			othis.div = document.getElementById("container");
			othis.div.innerHTML = "";
			othis.div.style.display = "none";
		}
		else
		{
			//Build the key to search in localStorage
			key = "http://localhost/getBooks.php?read=" + othis.read.value;
			
			if(localStorage[key])//We need to check in cache
			{
				othis.div.innerHTML  = "";
				booklist = JSON.parse(localStorage[key]);
				
				for(i=0;i<booklist.length;i++)
				{
					newdiv = document.createElement("div");
					newdiv.innerHTML = booklist[i];
					newdiv.className = "suggest";
				
					othis.div.appendChild(newdiv);
					
					//Now register for the click
					newdiv.onclick = othis.setBook;
				}
				//Show the container div
				othis.div.style.display = "block";
			
			}//End if check in cache
			
			else // no choice but to go to the server
			{
				othis.xhr.onreadystatechange = othis.processRes;
				othis.xhr.open("GET", "http://localhost/getBooks.php?read=" + othis.read.value,true);
			
				othis.xhr.send();
			}
		}
	} // end of fetchBook
	
	//Receive book suggestions from server and process
	this.processRes = function()
	{
		if(this.readyState == 4 && this.status == 200)
		{
			//First parse the JSON sent by the server
			//alert(this.responseURL);
			
			//Cleanup the div before populating new books
			books = JSON.parse(this.responseText);
			othis.div = document.getElementById("container");
			othis.div.innerHTML = "";

			if(books.length == 0)
			{
				//Server could not find any suggestions.
				othis.div.style.display = "none";
			}
			//Else we have some suggestions
			else
			{
				//loop thru and populate the container div
				for(i=0;i<books.length;i++)
				{
					newdiv = document.createElement("div");
					newdiv.innerHTML = books[i];
					newdiv.className = "suggest";
				
					othis.div.appendChild(newdiv);
					
					//Now register for the click
					newdiv.onclick = othis.setBook;
				}
				//Show the container div
				othis.div.style.display = "block";
				
				//Save to localStorage for later use
				localStorage[this.responseURL] = this.responseText;
			}
		}
	}//processRes over
	
	//When user selects a book from the list, set it into
	// the textbox and clear the container div
	this.setBook = function()
	{
		othis.read.value = this.innerHTML;
		othis.div.innerHTML = "";
		othis.div.style.display = "none";	
	}
}
obj = new Suggest();
