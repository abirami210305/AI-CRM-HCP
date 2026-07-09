import { useState } from "react";
import api from "../services/api";

function InteractionForm() {

  const [doctor, setDoctor] = useState("");
  const [hospital, setHospital] = useState("");
  const [date, setDate] = useState("");
  const [type, setType] = useState("Visit");
  const [notes, setNotes] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    const response = await api.post("/log-interaction", {
      doctor,
      hospital,
      date,
      type,
      notes,
    });

    alert(response.data.message);
  };

  return (
    <form onSubmit={handleSubmit}>

      <label>Doctor Name</label>
      <input
        type="text"
        value={doctor}
        onChange={(e) => setDoctor(e.target.value)}
        placeholder="Enter doctor name"
      />

      <label>Hospital</label>
      <input
        type="text"
        value={hospital}
        onChange={(e) => setHospital(e.target.value)}
        placeholder="Enter hospital name"
      />

      <label>Interaction Date</label>
      <input
        type="date"
        value={date}
        onChange={(e) => setDate(e.target.value)}
      />

      <label>Interaction Type</label>

      <select
        value={type}
        onChange={(e) => setType(e.target.value)}
      >
        <option>Visit</option>
        <option>Call</option>
        <option>Video Meeting</option>
      </select>

      <label>Notes</label>

      <textarea
        rows="5"
        value={notes}
        onChange={(e) => setNotes(e.target.value)}
        placeholder="Write interaction notes"
      />

      <button type="submit">
        Save Interaction
      </button>

    </form>
  );
}

export default InteractionForm;