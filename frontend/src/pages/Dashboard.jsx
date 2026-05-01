import { useEffect, useState } from "react";

import API from "../services/api";

import ESGScoreCard from "../components/ESGScoreCard";
import ESGRadarChart from "../components/ESGRadarChart";
import ESGTrendChart from "../components/ESGTrendChart";
import EvidenceViewer from "../components/EvidenceViewer";
import GreenwashingPanel from "../components/GreenwashingPanel";
import CompanySearch from "../components/CompanySearch";
import PortfolioAnalyzer from "../components/PortfolioAnalyzer";
import ControversyTimeline from "../components/ControversyTimeline";
import PeerComparison from "../components/PeerComparison";
import ESGScreener from "../components/ESGScreener";
import DownloadReport from "../components/DownloadReport";


function Dashboard() {

  const [ticker, setTicker] = useState("AAPL");

  const [scoreData, setScoreData] = useState(null);
  const [greenwashingData, setGreenwashingData] = useState(null);
  const [trendData, setTrendData] = useState([]);
  const [newsData, setNewsData] = useState([]);

  const [selectedType, setSelectedType] = useState("all");

  const [loading, setLoading] = useState(false);


  const loadData = async () => {
    try {

      setLoading(true);

      const scoreRes = await API.get(`/score/${ticker}`);
      const greenRes = await API.get(`/greenwashing/${ticker}`);
      const trendRes = await API.get(`/history/${ticker}`);
      const newsRes = await API.get(`/news/${ticker}`);

      // ✅ UPDATED (handle new API format)
      setScoreData(scoreRes.data?.data || scoreRes.data);
      setGreenwashingData(greenRes.data?.data || greenRes.data);
      setTrendData(trendRes.data?.data || trendRes.data || []);
      setNewsData(newsRes.data?.data || newsRes.data || []);

    } catch (err) {
      console.error("Dashboard error:", err);
    } finally {
      setLoading(false);
    }
  };


  useEffect(() => {
    loadData();
  }, []);


  if (loading || !scoreData || !greenwashingData) {
    return (
      <div style={{
        minHeight: "100vh",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        background: "#020617",
        color: "white",
        fontSize: "28px"
      }}>
        Loading ESG Dashboard...
      </div>
    );
  }


  // =========================
  // SAFE EVIDENCE
  // =========================
  const evidence = scoreData.evidence_quotes || {
    environmental: [],
    social: [],
    governance: []
  };


  let filteredQuotes = [];

  if (selectedType === "environment") {
    filteredQuotes = evidence.environmental;
  } else if (selectedType === "social") {
    filteredQuotes = evidence.social;
  } else if (selectedType === "governance") {
    filteredQuotes = evidence.governance;
  } else {
    filteredQuotes = [
      ...evidence.environmental,
      ...evidence.social,
      ...evidence.governance
    ];
  }


  return (
    <div style={{
      background: "#020617",
      minHeight: "100vh",
      color: "white",
      padding: "30px"
    }}>

      {/* HEADER */}
      <div style={{ textAlign: "center", marginBottom: "40px" }}>
        <h1 style={{ fontSize: "48px" }}>
          ESG AI Platform
        </h1>
        <p style={{ color: "#94a3b8" }}>
          AI-Powered ESG Intelligence Dashboard
        </p>
      </div>


      {/* SEARCH */}
      <CompanySearch
        ticker={ticker}
        setTicker={setTicker}
        onSearch={loadData}
      />


      {/* SCORE CARDS */}
      <div style={{
        display: "flex",
        gap: "20px",
        justifyContent: "center",
        marginTop: "40px",
        flexWrap: "wrap"
      }}>

        <ESGScoreCard
          title="Environmental"
          score={scoreData.environmental_score}
          onClick={() => setSelectedType("environment")}
        />

        <ESGScoreCard
          title="Social"
          score={scoreData.social_score}
          onClick={() => setSelectedType("social")}
        />

        <ESGScoreCard
          title="Governance"
          score={scoreData.governance_score}
          onClick={() => setSelectedType("governance")}
        />

        <ESGScoreCard
          title="Total ESG"
          score={scoreData.total_score}
          onClick={() => setSelectedType("all")}
        />

      </div>


      {/* PEER */}
      <PeerComparison />

      {/* RADAR */}
      <ESGRadarChart data={scoreData} />

      {/* TREND */}
      <ESGTrendChart trendData={trendData} />

      {/* NEWS */}
      <ControversyTimeline news={newsData} />

      {/* EVIDENCE */}
      <EvidenceViewer quotes={filteredQuotes} />

      {/* GREENWASHING */}
      <GreenwashingPanel flags={greenwashingData.flags} />

      {/* PORTFOLIO */}
      <PortfolioAnalyzer />

      {/* SCREENER */}
      <ESGScreener />

      {/* PDF EXPORT */}
      <div style={{ marginTop: "40px", textAlign: "center" }}>
        <DownloadReport ticker={ticker} />
      </div>

    </div>
  );
}

export default Dashboard;