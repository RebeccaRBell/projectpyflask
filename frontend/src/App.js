import React, { useState, useEffect } from "react";
import "./App.css";
import UserObj from "./components/UserObj";

function App() {
	const [users, setUsers] = useState([]);

	useEffect(() => {
		fetch("/api/users").then((res) =>
			res.json().then((users) => {
				setUsers(users);
			})
		);
	}, []);

	return (
		<div className="App">
			<header className="App-header">
				<h1>React and Flask</h1>
				<ul>
					{users.map((user, index) => (
						<div key={index}>
							<UserObj user={user} />
						</div>
					))}
				</ul>
			</header>
		</div>
	);
}

export default App;
