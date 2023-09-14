import './userobj.css'

const UserObj = ({user}) => {
  return (
    <div className='outer-container'>
    <div className="container">
      <p>Id: {user[0]}</p>
      <p>Name: {user[1]} {user[2]} {user[3]}</p>
      <p>Email: {user[4]}</p> 
      <p>Username: {user[5]}</p>
    </div>
    </div>
  )
}
export default UserObj