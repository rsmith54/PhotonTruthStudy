#include "GaudiKernel/DeclareFactoryEntries.h"

// Algs
#include "../PhotonTruthAlg.h"
#include "../ZbosonTruthAlg.h"

DECLARE_ALGORITHM_FACTORY(PhotonTruthAlg)
DECLARE_ALGORITHM_FACTORY(ZbosonTruthAlg)

DECLARE_FACTORY_ENTRIES(PhotonTruthStudy) {
  DECLARE_ALGORITHM(PhotonTruthAlg)
  DECLARE_ALGORITHM(ZbosonTruthAlg)
}
