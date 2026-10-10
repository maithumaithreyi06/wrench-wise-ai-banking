
# AI Banking Assistant

## Project Overview
A simulated multi-agent banking application built using Python
and Streamlit.

## Agents
1. Customer / Banking Agent
2. Risk / Fraud Agent
3. Credit / Loan Agent
4. Banking Help Agent
5. Supervisor / Orchestrator Agent

## Features
- Demo account balance
- Transaction history
- Rule-based transaction risk checks
- Simplified loan eligibility estimation
- Supervisor-based request routing
- Interactive web interface

## Installation
python -m pip install -r requirements.txt

## Run Application
python -m streamlit run app.py

## Run Tests
python -m unittest test_agents.py -v

## Limitations
This is an educational simulation using fictional data.
It does not connect to a real bank. Routing is keyword-based,
and the current version does not integrate an LLM.
