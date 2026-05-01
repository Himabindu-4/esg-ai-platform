import {
  Radar,
  RadarChart,
  PolarGrid,
  PolarAngleAxis,
  PolarRadiusAxis,
  ResponsiveContainer,
} from "recharts";


function ESGRadarChart({ data }) {

  const chartData = [

    {
      subject: "Environmental",
      score: data.environmental_score,
    },

    {
      subject: "Social",
      score: data.social_score,
    },

    {
      subject: "Governance",
      score: data.governance_score,
    },
  ];

  return (

    <div
      style={{
        background: "#1e293b",
        padding: "20px",
        borderRadius: "12px",
        marginTop: "40px",
      }}
    >

      <h2
        style={{
          color: "white",
          marginBottom: "20px",
        }}
      >
        ESG Radar Analysis
      </h2>

      <ResponsiveContainer width="100%" height={400}>

        <RadarChart data={chartData}>

          <PolarGrid />

          <PolarAngleAxis dataKey="subject" />

          <PolarRadiusAxis
            angle={30}
            domain={[0, 100]}
          />

          <Radar
            name="ESG Score"
            dataKey="score"
            stroke="#38bdf8"
            fill="#38bdf8"
            fillOpacity={0.6}
          />

        </RadarChart>

      </ResponsiveContainer>

    </div>
  );
}

export default ESGRadarChart;