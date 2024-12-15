<!DOCTYPE html> 
<html>
<head>
<title>Form Validation</title>
<h1>Form Validation</h1>
</head> 
<body> 
<form id="myForm"> 
<label for="name">Name:</label> <input type="text" id="name" name="name"><br><br>  
<label for="email">Email:</label> <input type="text" id="email" name="email"><br><br>  
<label for="mobile">Mobile Number:</label> <input type="text" id="mobile" name="mobile"><br><br>
<label>Gender:</label> <input type="radio" id="male" name="gender" value="Male">Male 
<input type="radio" id="female" name="gender" value="Female">Female<br><br>
<label>Hobbies:</label> <input type="checkbox" id="reading" name="hobbies" value="Reading">Reading <input type="checkbox" id="traveling" name="hobbies" value="Traveling">Traveling<br><br>  
<input type="submit" value="Submit" onclick="countFormElements()"> 
</form>
<script> document.getElementById("myForm").addEventListener("submit", function(event) { event.preventDefault();
//Validation for email format
 var email = document.getElementById("email").value;   
var emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
 // Validation for mobile number length (assuming 10 characters)
var mobile = document.getElementById("mobile").value;  
// Check if any required field is left empty 
var name = document.getElementById("name").value;  
if (name === "" || email === "" || mobile === "" ) 
{ 
alert("Please fill in all required fields.");
}
else if (!emailPattern.test(email)) 
{
 alert("Invalid email format. Please enter a valid email address.");   
}
else if (mobile.length !== 10 || isNaN(mobile)) 
{
 alert("Mobile number should be 10 digits numeric.");
}
 else 
{
// Form is valid, you can submit it or perform further actions here 
alert("Form submitted successfully!"); 
}
}); 
</script>
</body>
</html
