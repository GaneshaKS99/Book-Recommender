<?php header('Access-Control-Allow-Origin: *');
	//Get the book part that was sent by the client
	extract($_GET); //$read has the data
	$file = fopen("books2.txt", "r");
	$arr = array();
	//Read the file contents, one line at a time and see
	// if we have an initial string match. If so, pick up
	// that line and add it to an array. We can send it
	// as a JSON to the client.
	while($line = fgets($file))
	{
		$book = trim($line);
		if(strncasecmp($read, $book, strlen($read)) == 0)
		{
			$arr[] = $book;
		}
	}
	echo json_encode($arr);
?>