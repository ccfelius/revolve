from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import Optional, List
    from pyrevolve.revolve_bot import RevolveBot
    from pyrevolve.genotype import Genotype


class Individual:
    def __init__(self, genotype: Genotype, phenotype: Optional[RevolveBot] = None):
        """
        Creates an Individual object with the given genotype and optionally the phenotype.

        :param genotype: genotype of the individual
        :param phenotype (optional): phenotype of the individual
        """
        self.genotype: Genotype = genotype
        self.phenotype: RevolveBot = phenotype
        self.fitness: Optional[float] = None
        self.parents: Optional[List[Individual]] = None
        self.failed_eval_attempt_count: int = 0

    def develop(self):
        """
        Develops genotype into a intermediate phenotype
        """
        if self.phenotype is None:
            self.phenotype = self.genotype.develop()

    @property
    def id(self):
        _id = None
        if self.phenotype is not None:
            _id = self.phenotype.id
        elif self.genotype.id is not None:
            _id = self.genotype.id
        return _id

    def export_genotype(self, folder):
        self.genotype.export_genotype(f'{folder}/genotypes/genotype_{self.phenotype.id}.txt')

    def export_phenotype(self, folder):
        if self.phenotype is not None:
            # TODO "/phenotypes/phenotype_"
            self.phenotype.save_file(f'{folder}/phenotypes/{self.phenotype.id}.yaml', conf_type='yaml')

    def export_fitness(self, folder):
        """
        It's saving the fitness into a file. The fitness can be a floating point number or None
        :param folder: folder where to save the fitness
        """
        with open(f'{folder}/fitness_{self.id}.txt', 'w') as f:
            f.write(str(self.fitness))

    def export(self, folder):
        self.export_genotype(folder)
        self.export_phenotype(folder)
        self.export_fitness(folder)

    def __repr__(self):
        return f'Individual_{self.id}({self.fitness})'
