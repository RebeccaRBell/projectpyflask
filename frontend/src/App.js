// Importing modules
import React, { useState, useEffect } from "react";
import "./App.css";

function App() {
	// usestate for setting a javascript
	// object for storing and using data
	const [data, setdata] = useState({
		id: 0,
		title: "",
		firstname: "",
		lastname: "",
	});

	// Using useEffect for single rendering
	useEffect(() => {
		// Using fetch to fetch the api from
		// flask server it will be redirected to proxy
		fetch("/data").then((res) =>
			res.json().then((data) => {
				// Setting a data from api
				setdata({
					id: data.id,
					title: data.title,
					firstname: data.firstname,
					lastname: data.lastname,
				});
			})
		);
	}, []);

	return (
		<div className="App">
			<header className="App-header">
				<h1>React and flask</h1>
				{/* Calling a data from setdata for showing */}
				<p>ID: {data.id}</p>
				<p>Title: {data.title}</p>
				<p>First Name: {data.firstname}</p>
				<p>Last Name: {data.lastname}</p>

			</header>
		</div>
	);
}

export default App;
