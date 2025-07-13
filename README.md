# UppaalTD: Formal Tower Defense Game

[![UPPAAL](https://img.shields.io/badge/UPPAAL-Model%20Checking-blue)](https://uppaal.org/)
[![Formal Methods](https://img.shields.io/badge/Formal%20Methods-TCTL-green)](https://en.wikipedia.org/wiki/Computation_tree_logic)
[![PDF Report](https://img.shields.io/badge/Report-PDF-red)](Report.pdf)

> **A comprehensive formal verification project modeling and analyzing a tower defense game using UPPAAL's timed automata and statistical model checking capabilities.**

## Project Overview

This project demonstrates advanced formal methods techniques by modeling a complete tower defense game in UPPAAL, featuring rigorous verification of temporal properties and statistical analysis of stochastic behaviors. The work showcases expertise in **concurrent systems modeling**, **real-time verification**, and **statistical model checking**.

### Research Highlights

- **Dual Modeling Approach**: Vanilla (deterministic) and Stochastic versions using exponential distributions
- **Comprehensive Verification**: TCTL properties, deadlock freedom, and timing constraints
- **Statistical Analysis**: UPPAAL SMC statistical model checking with 700+ enemy instances

## System Architecture

### Core Components

| Component | Description | Key Features |
|-----------|-------------|--------------|
| **GameTime** | Global game controller | Timeout management, deadlock prevention |
| **Turret** | Defense unit automaton | Scanning, targeting, reloading mechanics |
| **Enemy/EnemyP** | Adversarial entities | Coordinated movement, path selection |

### Game Elements

<div align="center">

| Enemies | | Turrets | |
|---------|--|---------|--|
| 🔵 **Circle** | Fast, low damage | 🔫 **Basic** | Standard range/damage |
| 🟩 **Square** | Slow, high damage | 💥 **Cannon** | High damage, slow reload |
| | | 🎯 **Sniper** | Long range, precise |

</div>

## Verification Results

### Formal Properties Verified

#### Vanilla Version (Deterministic)
- **Deadlock Freedom**: System never reaches deadlock states
- **Path Correctness**: Enemies never deviate from designated routes
- **Timing Bounds**: All enemies reach targets within calculated time limits
- **Configuration Analysis**: Win/loss determination across different turret placements

#### Stochastic Version (Statistical)
- **Survival Probability**: ~10% tower survival rate in baseline configuration
- **Expected Damage Time**: Statistical estimation of first damage occurrence
- **Performance Metrics**: Enemy throughput, elimination rates, tower health decay

### Configuration Comparison

| Configuration | Strategy | Outcome |
|--------------|----------|---------|
| **Config 1** (Baseline) | Given example | Mixed results (10% survival) |
| **Config 2** (Optimized) | Strategic placement | Higher win probability |
| **Config 3** (Suboptimal) | Poor positioning | Higher loss rate |

## Technical Implementation: Design Choices and Advanced Modeling Techniques

- **Urgent Channels**: Immediate state transitions with `asap` broadcast
- **Committed Locations**: Reduced interleaving for deterministic paths  
- **Statistical SMC**: Exponential distributions for realistic timing
- **Template Parameterization**: Scalable enemy/turret instantiation
- **Automated Code Generation**: Python scripts for UPPAAL statistical model generation

## Statistical Analysis

The project includes comprehensive statistical model checking with:

- **700 Enemy Simulation**: Large-scale concurrent system analysis
- **Multiple Metrics**: Alive count, elimination rate, tower damage
- **Probabilistic Queries**: `Pr[]` and `E[]` operators for statistical inference
- **Visual Analytics**: Plots and histograms for result interpretation

## Tools & Technologies

- **UPPAAL**: Timed automata modeling and verification
- **TCTL**: Temporal logic property specification
- **Statistical MC**: Monte Carlo simulation engine
- **Python**: Automated code generation
- **LaTeX**: Professional documentation

## Key Achievements

1. **Complex System Modeling**: Successfully modeled concurrent tower defense with 700+ entities
2. **Formal Verification**: Proved critical safety and liveness properties
3. **Statistical Validation**: Quantified system performance under uncertainty
4. **Scalable Architecture**: Automated generation for large-scale verification
5. **Comprehensive Analysis**: Both deterministic and stochastic behavior characterization

## Academic Context

**Course**: Formal Methods for Concurrent and Real-Time Systems  
**Institution**: Advanced Computer Science Program  
**Focus Areas**: Model checking, temporal logic, statistical verification  
**Applications**: Safety-critical systems, concurrent algorithms, real-time analysis

## Documentation

- **[Complete Report](Report.pdf)**: Detailed analysis, methodology, and results
- **[Homework Assignment](Homework.pdf)**: Original project specifications
- **[UPPAAL Models](UppaalTD.xml)**: Vanilla version implementation
- **[Stochastic Models](UppaalTD-Stochastic.xml)**: Statistical version with SMC

---

<div align="center">

**Demonstrating expertise in formal verification, concurrent systems, and statistical analysis through practical application to interactive system modeling.**

*Authors: Andrea Torti, Lorenza D'Amario*

</div>
