// Importing modules
import React, { useState, useEffect } from "react";
import "./App.css";

function App() {
	// usestate for setting a javascript
	// object for storing and using data
	const [users, setusers] = useState();

	useEffect(() => {
		fetch("/data").then((res) =>
			res.json().then((users) => {
				setusers(users);
			})
		);
	}, []);

	return (
		<div className="App">
			<header className="App-header">
				<h1>React and flask</h1>
				<p>User Data: {users}</p>
			</header>
		</div>
	);
}

export default App;
