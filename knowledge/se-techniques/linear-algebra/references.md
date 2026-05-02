# References

Linear algebra is a mature mathematical field; the references below
are the specific sources that connect it to the three applications
in `how-it-works.md`.

## On graph spectra and control graphs

- Chung, F.R.K. (1997). *Spectral Graph Theory.* CBMS Regional
  Conference Series in Mathematics, AMS. The standard reference for
  Laplacian eigenvalues, algebraic connectivity, and the spectral
  bounds used to read connectivity off the spectrum.
- Newman, M.E.J. (2010). *Networks: An Introduction.* Oxford
  University Press. Practical treatment of eigenvector centrality
  and PageRank as applied to organisational and social graphs.
- Bonacich, P. (1972). "Factoring and weighting approaches to status
  scores and clique identification." *Journal of Mathematical
  Sociology*, 2(1), 113–120. The original eigenvector-centrality
  paper.

## On the Design Structure Matrix

- Steward, D.V. (1981). "The Design Structure System: A Method for
  Managing the Design of Complex Systems." *IEEE Transactions on
  Engineering Management*, EM-28(3), 71–74. The original DSM
  paper.
- Eppinger, S.D. & Browning, T.R. (2012). *Design Structure Matrix
  Methods and Applications.* MIT Press. The standard reference;
  covers block-triangularisation and its use across product, process,
  and organisation matrices.
- Tarjan, R. (1972). "Depth-first search and linear graph
  algorithms." *SIAM Journal on Computing*, 1(2), 146–160. The
  strongly-connected-components algorithm that does the
  block-triangularisation in practice.

## On PCA and SVD for feature matrices

- Jolliffe, I.T. (2002). *Principal Component Analysis* (2nd ed.).
  Springer. The standard reference. Chapters on small-sample
  pitfalls are directly relevant to this project's catalogue
  sizes.
- Golub, G.H. & Van Loan, C.F. (2013). *Matrix Computations* (4th
  ed.). Johns Hopkins. Numerical reference for SVD.
- Czekanowski, J. (1909). "Zur Differentialdiagnose der
  Neandertalgruppe." *Korrespondenz-Blatt der Deutschen Gesellschaft
  für Anthropologie*, 40, 44–47. The earliest example of
  ordering a similarity matrix by what would later be called
  spectral methods — useful as a historical anchor.

## On the false-precision trap

- Gould, S.J. (1981). *The Mismeasure of Man.* W.W. Norton. The
  classic critique of factor analysis applied to socially-loaded
  measurements; the methodological warnings transfer directly to
  the systems-engineering setting.
- Gigerenzer, G. (2004). "Mindless statistics." *The Journal of
  Socio-Economics*, 33(5), 587–606. On the temptation to mistake
  computational outputs for substantive findings.

## Relation to this project

Linear algebra is treated here as a *narrowly scoped complement* to
the qualitative SE techniques. The project does not adopt it as a
general analysis layer because the dominant uncertainty in the
social-systems catalogue lives in the matrix entries, not in the
matrix structure — and linear algebra cannot fix that.
