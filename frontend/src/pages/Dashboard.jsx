import Header from "../components/Header";
import InteractionForm from "../components/InteractionForm";
import ChatBox from "../components/ChatBox";

function Dashboard() {
  return (
    <div className="container">
      <Header />
      <InteractionForm />
      <hr />
      <ChatBox />
    </div>
  );
}

export default Dashboard;