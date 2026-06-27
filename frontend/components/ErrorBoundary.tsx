import React, { Component, ErrorInfo, ReactNode } from "react";

interface Props {
  children: ReactNode;
}

interface State {
  hasError: boolean;
  error: Error | null;
}

export default class ErrorBoundary extends Component<Props, State> {
  constructor(props: Props) {
    super(props);
    this.state = { hasError: false, error: null };
  }

  static getDerivedStateFromError(error: Error): State {
    return { hasError: true, error };
  }

  componentDidCatch(error: Error, info: ErrorInfo) {
    console.error("[ErrorBoundary] 未捕获异常:", error);
    console.error("[ErrorBoundary] 组件栈:", info.componentStack);
  }

  handleReload = () => {
    this.setState({ hasError: false, error: null });
    window.location.reload();
  };

  render() {
    if (this.state.hasError) {
      return (
        <div
          style={{
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
            justifyContent: "center",
            height: "100vh",
            gap: 16,
            fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif",
            background: "#f8f7f4",
            color: "#2d2d2d",
            padding: 24,
            textAlign: "center",
          }}
        >
          <div style={{ fontSize: 48, opacity: 0.3, marginBottom: 8 }}>⚠</div>
          <h2 style={{ fontSize: 22, fontWeight: 600, margin: 0 }}>
            应用发生意外错误
          </h2>
          <p
            style={{
              fontSize: 14,
              color: "#8a8a8a",
              maxWidth: 480,
              lineHeight: 1.6,
              margin: 0,
            }}
          >
            抱歉，应用遇到了未处理的异常。请尝试重新加载页面，如果问题持续出现请联系支持。
          </p>
          {this.state.error && (
            <details
              style={{
                marginTop: 8,
                fontSize: 12,
                color: "#c45a5a",
                background: "rgba(196,90,90,0.06)",
                padding: "12px 16px",
                borderRadius: 8,
                maxWidth: 520,
                textAlign: "left",
                wordBreak: "break-all",
              }}
            >
              <summary style={{ cursor: "pointer", fontWeight: 500 }}>
                错误详情
              </summary>
              <pre style={{ marginTop: 8, whiteSpace: "pre-wrap" }}>
                {this.state.error.message}
              </pre>
            </details>
          )}
          <button
            onClick={this.handleReload}
            style={{
              marginTop: 8,
              padding: "10px 28px",
              fontSize: 14,
              fontWeight: 500,
              color: "#fff",
              background: "#6b9fd4",
              border: "none",
              borderRadius: 8,
              cursor: "pointer",
              transition: "background 0.15s",
            }}
            onMouseEnter={(e) =>
              (e.currentTarget.style.background = "#5a8ec4")
            }
            onMouseLeave={(e) =>
              (e.currentTarget.style.background = "#6b9fd4")
            }
          >
            重新加载
          </button>
        </div>
      );
    }

    return this.props.children;
  }
}
