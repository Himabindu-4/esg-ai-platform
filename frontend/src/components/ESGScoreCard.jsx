function ESGScoreCard({ title, score, onClick }) {

  return (
    <div
      onClick={onClick}
      style={{
        background: "#1e293b",
        padding: "20px",
        borderRadius: "12px",
        cursor: "pointer",
        minWidth: "200px",
        textAlign: "center",
        transition: "0.2s",
      }}
      onMouseEnter={(e) =>
        (e.currentTarget.style.transform = "scale(1.05)")
      }
      onMouseLeave={(e) =>
        (e.currentTarget.style.transform = "scale(1)")
      }
    >

      <h3 style={{ color: "#94a3b8" }}>
        {title}
      </h3>

      <h1 style={{ color: "#38bdf8" }}>
        {score}
      </h1>

    </div>
  );
}

export default ESGScoreCard;