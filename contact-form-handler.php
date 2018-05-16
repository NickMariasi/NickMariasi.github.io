<?php

	$name = $_POST['firstname'];
	$visitor_email = $_POST['E-Mail'];
	$message = $_POST['message'];
	$lastname = $_POST['lastname'];
	
	$email_from = 'Nickmariasi5444@gmail.com';
	
	$email_subject = "New Form Submission";
	
	$email_body = "Name: $name.\n".
					"Email: $visitor_email.\n".
					"User Message: $message.\n".
					"Last Name: $lastname.\n";
					
	$to = "nickmariasi@yahoo.com";
	
	$headers = "From: $email_from \r\n";
	
	$headers = "Reply-To: $visitor_email \r\n";
	
	mail($to,$email_subject,$email_body,$headers);
	
	header("Location: contact.html");
	
?>